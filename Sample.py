import re
from pathlib import Path
import requests
from bs4 import BeautifulSoup



url = "https://bulletin.temple.edu/undergraduate/science-technology/computer-information-science/computer-science-bs/#requirementstext"

html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")
img_container = soup.find(class_="container-post__inner")

output_folder = Path('いらすとや9')
output_folder.mkdir(exist_ok=True)
for item in img_container.find_all("img"):
    img_url = item.attrs["src"]
    print(img_url)
    filename = re.search(".*\/(.*gif|.*jpg|.*JPG)$", img_url)

    try:
        save_path = output_folder.joinpath(filename.group(1))
    except:
        print("No group")
        continue
    print("downloading :" + str(save_path))
    try:
        image = requests.get(img_url)
        # ④-②.保存先のファイルパスにデータを保存
        open(save_path, 'wb').write(image.content)
        # ④-③.保存したファイル名を表示
        print("done")
    except:
        print("Failed :" + str(save_path))
    #
