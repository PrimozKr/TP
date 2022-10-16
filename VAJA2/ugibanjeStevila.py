import random

x= random.randrange(0,30)
print(x)
s_poskusou=5
while s_poskusou > 0:
    poskus = input("vnesi stevilo: ")
    poskus = int(poskus)
    if x == poskus:
        print("zmaga")
        break
    elif poskus < x:
        print("vnesli ste premajhno stevilko")

    else:
        print("vnesli ste preveliko stevilko")

    s_poskusou=s_poskusou -1

