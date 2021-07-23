import re
from pathlib import Path
import requests
from bs4 import BeautifulSoup

url = "https://bulletin.temple.edu/undergraduate/science-technology/computer-information-science/computer-science-bs/#requirementstext"

html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")

tables = soup.findAll(class_="sc_courselist")

# Getting table body
tableBody = tables[0].find("tbody")

# Getting rows from table body
rows = tableBody.find_all("tr")

# Prepare data list
data = []

# Loop through list of rows
for row in rows:
    listCol = []
    link = ""

    # Find all cols in a row
    cols = row.find_all("td")

    # If there is no link attached with course ID, that means its invalid row so skip
    if not cols[0].find("a"):
        continue
    else:
        # Else get link
        link = a = cols[0].find("a").get("href")

    for col in cols:
        # Get text
        text = col.text.strip()
        # If text has "or", remove it
        if text[0:2] == "or":
            text = text[3:]
        # Append result to the list
        listCol.append(text)

    # Insert link
    listCol.insert(2, link)

    # Append result
    data.append(listCol)

# Print out data
for row in data:
    print(row[0] + "\t" + row[1] + "\t" + "https://bulletin.temple.edu/" + row[2])
