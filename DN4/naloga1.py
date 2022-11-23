import json


podatki = { "name": "john",
            "age" : "30",
            "city" : "New York "}


pretvorba= json.dumps(podatki)

print(pretvorba)