import requests
import redis

# Connect to Redis
r = redis.StrictRedis(
    host='redis-12939.c322.us-east-1-2.ec2.cloud.redislabs.com',
    port=12939,
    password='GVBLTziwvl4AvWqgnOJQP8FW6PLU2gDl',
    decode_responses=True  # This allows decoding responses as strings
)

api_key = "jBsbenx0gN2VODKm3VLz11IeaKJxzaaMdTHUn4nc"
url = "https://api.nasa.gov/planetary/apod"
params = {
    'api_key': api_key,
    'count': 20  # Fetch 20 records
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    for apod in data:
        # Use date as key and title as value to insert into Redis
        r.set(apod['date'], apod['title'])
        print(f"Inserted {apod['title']} with key {apod['date']} into Redis")
else:
    print("Error:", response.status_code)
    print(response.text)
