import requests
import time as t
target=input("Target: ")
messaggio=input("Messaggio: ")
myobj = {"question":f"{messaggio}"}
url = f'https://ngl.link/{target}/'
while True:
  for i in range(12):
    x = requests.post(url, json = myobj)
    print(x)
  t.sleep(90)
