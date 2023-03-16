import requests
from bs4 import BeautifulSoup

URL = "https://row52.com/Search/?YMMorVin=YMM&Year=2000-2005&V1=&V2=&V3=&V4=&V5=&V6=&V7=&V8=&V9=&V10=&V11=&V12=&V13=&V14=&V15=&V16=&V17=&ZipCode=95023&Page=1&ModelId=1150&MakeId=90&LocationId=&IsVin=false&Distance=100"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

car_elements = soup.find_all("div", class_="list-row")

for car_element in car_elements:
    vin_element = car_element.find("a", class_="vin")

print(vin_element.text.strip())
print()
