from bs4 import BeautifulSoup
import requests
                                            # use requests to fetch the page
url = "https://www.wausauwesthoops.com/page/show/8246384-varsity"
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, "lxml")

                                            # Get all rows in the table
rows = schedule_table.find_all("tr")

                                            # Initialize an empty list to store schedule data
schedule_data = []

                                            # Loop through each row
for row in rows:
                                                # Extract date, time, opponent, and location from corresponding cells
    date = row.find("td", class_="date").text
    time = row.find("td", class_="time").text
    opponent = row.find("td", class_="opponent").text
    location = row.find("td", class_="location").text

                                                # Add data to the list
    schedule_data.append({
        "date": date,
        "time": time,
        "opponent": opponent,
        "location": location,
    })

                                            # Print the extracted schedule data
print(schedule_data)
