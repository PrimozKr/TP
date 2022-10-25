for prastevilo in range (1, 51):
    count = 0
    for i in range(2, (prastevilo//2 + 1)):
        if(prastevilo % i == 0):
            count = count + 1
            break

    if (count == 0 and prastevilo != 1):
        print(prastevilo,end = '  ')