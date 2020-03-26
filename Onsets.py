
from sorting_methods import Insertion_up
from sorting_methods import bubble_up
lista = ([1,2,6,4,5],3)
lista_1 = ([1,2,6,4,5],3)

def Onsets_By_Insertion(data):
    numbers = data[0]
    minimal = data[1]
    count = 0
    tuple = ([],[])
    for i in range(len(numbers)):
        if count <=2:
            if numbers[i] > minimal:

                tuple[0].append(i)
                tuple[1].append(numbers[i])
                count = count+1
            else: pass
        else: break
    Insertion_up(tuple)
    indexes_sorted = tuple[0]
    return indexes_sorted

def Onsets_By_Bubble(data):
    numbers = data[0]
    minimal = data[1]
    count = 0
    tuple = ([],[])
    for i in range(len(numbers)):
        if count <=2:
            if numbers[i] > minimal:

                tuple[0].append(i)
                tuple[1].append(numbers[i])
                count = count+1
            else: pass
        else: break
    bubble_up(tuple)
    indexes_sorted = tuple[0]
    return indexes_sorted

demo_list = ([1,2,6,4,5],3)

OUT1 = Onsets_By_Insertion(demo_list)
OUT2 = Onsets_By_Bubble(demo_list)

print(OUT1)
print(OUT2)


