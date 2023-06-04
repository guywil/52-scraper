import requests
from bs4 import BeautifulSoup

URL = "https://row52.com/Search/?YMMorVin=YMM&Year=2001-2005&V1=&V2=&V3=&V4=&V5=&V6=&V7=&V8=&V9=&V10=&V11=&V12=&V13=&V14=&V15=&V16=&V17=&ZipCode=95023&Page=1&ModelId=1150&MakeId=90&LocationId=&IsVin=false&Distance=100"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# only prints first vin off page
#car_vin = soup.find('a', {'class':'vin'}).get_text()

#for word in soup.find_all('vin'):

#    car_vin = word.get_text()
#car_vin = word.get_text()
## kinda works
car_vin = soup.find_all(class_='vin')

if car_vin == 0:
    print('No vins available at the moment')
else:
    print(car_vin.text)
