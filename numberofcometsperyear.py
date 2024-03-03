import requests
import redis
import matplotlib.pyplot as plt

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

# Initialize dictionary to store the count of comets for each year
comets_per_year = {}

if response.status_code == 200:
    data = response.json()
    for apod in data:
        # Extract year from date
        year = apod['date'][:4]

        # Increment count of comets for the current year
        if year in comets_per_year:
            comets_per_year[year] += 1
        else:
            comets_per_year[year] = 1

        # Use date as key and title as value to insert into Redis
        r.set(apod['date'], apod['title'])
        print(f"Inserted {apod['title']} with key {apod['date']} into Redis")
else:
    print("Error:", response.status_code)
    print(response.text)

# Create line graph
years = list(comets_per_year.keys())
num_comets = list(comets_per_year.values())

plt.figure(figsize=(10, 6))
plt.plot(years, num_comets, marker='o')
plt.title('Number of Comets per Year')
plt.xlabel('Year')
plt.ylabel('Number of Comets')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
