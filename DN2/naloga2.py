our_list = [1,2,3,4,5,6,7]
our_dict = {
    "a": 2,
    "b": 5,
    "c": 8,
    "d": 12,
    "e": 357,
    "f": 12
}
our_tuple = (357, 12, 12, 8, 5, 2, 2)

x=our_list[4]


#odstranimo vrednost na indexu 4
our_list.remove(our_list[4])
print(our_list)

#vrednos iz indexa 4 dodamo v dic pod kjuč "d"
our_dict.update(d=x)

#izpis vrednosti
for values in our_dict.values():
    print(values,end = ' ')

#vrednosti iz our_dict  shranimo v nov tuple -my_tuple
my_tuple = our_dict
print('\n' ,my_tuple)

#primerjamo če sta nov tuple in podani tuple enaka 

print(my_tuple == our_tuple)


