import requests

url=input("vnesite url spletne strani:",)


def get_html(url):
    
    page=requests.get(url)
    
    if page.status_code ==200:
        print(page.text)

    else:
        print("false")


get_html(url)

 

