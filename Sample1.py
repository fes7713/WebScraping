import re
from pathlib import Path
import requests
from bs4 import BeautifulSoup
import os


url = "https://bulletin.temple.edu/undergraduate/science-technology/computer-information-science/computer-science-bs/#requirementstext"

html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")
# sc_courselist

tables = soup.findAll(class_="sc_courselist")
tableBodies = []
for table in tables:
    tableBodies.append(table.find("tbody"))

def scrape(tableBody, continueConditions):
    courseRows = tableBody.find_all("tr")

    data = []

    for course in courseRows:
        listRow = []
        cols = course.find_all("td")
        for col in cols:
            listRow.append(col.text.strip())

        data.append(listRow)

    rows = len(data)

    result = []
    for i in range(0, rows):
        if data[i][0] == "Mathematics":
            break

        checkCondition = False
        for condition in continueConditions:
            if data[i][0][0:len(condition)] == condition:
                checkCondition = True

        if checkCondition:
            continue

        if data[i][0][0:2] == "or":
            result.append(data[i][0][3:] + "\t" + data[i][1])
        else:
            result.append(data[i][0] + "\t" + data[i][1])
    return result

table = scrape(tableBodies[0], ["Select", "Computer"])
for row in table:
    print(row)

table = scrape(tableBodies[1], ["Select", "Biology", "Chemistry", "Earth", "Physics"])
for row in table:
    print(row)
