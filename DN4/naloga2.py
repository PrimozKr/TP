import math
from statistics import mean 
from bisect import bisect_left

vnesene_vrednosti=input("Vnesite poljubne številke ločene z presledkom : ")

#pretvorimo v list
vrednosti_list=vnesene_vrednosti.split()

#pretvorimo v int
for i in range(len(vrednosti_list)):
    vrednosti_list[i]=int(vrednosti_list[i])



najmanjsi_element=min(vrednosti_list)
print("najmanjši element je: ",najmanjsi_element)

navecji_element=max(vrednosti_list)
print("največji element je: ", navecji_element)


povprecje=mean(vrednosti_list)
print("povprečje je:",povprecje)


def closest(vrednosti_list, povprecje):
    return vrednosti_list[min(range(len(vrednosti_list)), key = lambda i: abs(vrednosti_list[i]-povprecje))]

print("najbližja vrednost povprečju je: ",closest(vrednosti_list, povprecje))






