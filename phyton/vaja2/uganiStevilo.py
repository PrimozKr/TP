import random 

x=random.randrange(0,30)

while s_poskusou > 0:
    poskus= input("Vnesi stevilo")
    poskus=int(poskus)
    if x == poskus:
        print("Zmaga")
        break
    elif poskus <x:
        print("vnesli ste premajhno številko")
    else:
            print("vnesli ste preveliko številko")


    s_poskusou =s_poskusou - 1









    
   
