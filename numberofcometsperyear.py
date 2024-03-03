import requests
import matplotlib.pyplot as plt

# Fetch APOD data
api_key = "jBsbenx0gN2VODKm3VLz11IeaKJxzaaMdTHUn4nc"
url = "https://api.nasa.gov/planetary/apod"

# Initialize dictionary to store records per year
records_per_year = {}

# Fetch data in chunks of 100 records
for page in range(20):  # Fetching 20 pages with 100 records each
    params = {
        'api_key': api_key,
        'count': 100,
        'start_date': f"{(2000-page)-1}-12-31",  # Fetch data starting from the end of 1999
        'end_date': f"{2000-page}-12-31"         # Fetch data until the end of the current year
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        # Process data to count records per year
        for apod in data:
            year = apod['date'][:4]
            if year in records_per_year:
                records_per_year[year] += 1
            else:
                records_per_year[year] = 1
    else:
        print("Error:", response.status_code)
        print(response.text)

# Sort dictionary by year
sorted_records_per_year = dict(sorted(records_per_year.items()))

# Extract years and record counts
years = list(sorted_records_per_year.keys())
num_records = list(sorted_records_per_year.values())

# Create line graph
plt.figure(figsize=(10, 6))
plt.plot(years, num_records, marker='o')
plt.title('Number of APOD Records per Year (Until 2000)')
plt.xlabel('Year')
plt.ylabel('Number of Records')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
