import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_countries_by_population"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

tables = soup.find_all("table", class_="wikitable")
print("Tables found:", len(tables))

if len(tables) == 0:
    print("No tables found")
    exit()

table = tables[0]
rows = table.find_all("tr")

data = []
for row in rows[1:]:
    cols = row.find_all("td")
    if len(cols) >= 4:
        data.append([c.text.strip() for c in cols[:4]])

df = pd.DataFrame(data, columns=["Country", "Population", "Percentage", "Date"])
df.to_csv("population_data.csv", index=False)

print("✅ Data scraped successfully")
