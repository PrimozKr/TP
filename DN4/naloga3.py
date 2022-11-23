import requests

x = requests.get('https://www.rtvslo.si/iskalnik?q=iskalni%20niz')

print(x.text)

