import re
from pathlib import Path
import requests
from bs4 import BeautifulSoup

url = "https://bulletin.temple.edu/undergraduate/science-technology/computer-information-science/computer-science-bs/#requirementstext"

html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")

table = soup.find(class_="sc_courselist")

tbody = table.find("tbody")




print(tableBody)
