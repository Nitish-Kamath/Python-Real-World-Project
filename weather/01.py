import requests
from bs4 import BeautifulSoup  #bs4 ->BeautifulSoup4
import datetime

res = datetime.datetime.now()



search = "weather in Patna "
url = f"https://www.google.com/search?&q={search}"


r = requests.get(url)
s = BeautifulSoup(r.text,"html.parser")   #html parser ->parse the website
update = s.find("div",class_="BNeawe").text

print(f"Temperature of your location @{res} is {update}")
# print(update)

