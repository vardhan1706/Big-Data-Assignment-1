import requests

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
        # Filter records below the year 2000
        if int(apod['date'][:4]) < 2000:
            print(apod['date'], apod['title'])
else:
    print("Error:", response.status_code)
    print(response.text)
