import requests
import json 

url=input("vnesite url spletne strani:",)


def get_api_data(url):
    x=requests.get(url)
    
    if x.status_code ==200:
        page=x.json()
        print(page)

    else:
        print("false")


get_api_data(url)
 
