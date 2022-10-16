a=input("vnesite prvo število: ")
b=input("Vnesite drugo število: ")
c=input("Vnesite tretje število: ")

print("prva izbrana  =",a)
a=int(a)
print(type(a))

print("druga izbrana  =",b)
b=int(b)
print(type(b))

print("tretja izbrana  =",c)
c=int(c)
print(type(c))

if (b==a and c<=a ):
    print("pogoj b==a in c <=a JE izpolnjen")
    

else:
    print("pogoj b==a in c<=a NI izpolnjen")
