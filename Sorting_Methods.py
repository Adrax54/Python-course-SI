def sortowanie_bąbelkowe(liczby):
    n = len(liczby)
    zmieniona = True
    while zmieniona == True:
        zmieniona = False
        for i in range(n-1):
            if liczby[i] > liczby[i+1]:
                liczby[i], liczby[i+1] = liczby[i+1],liczby[i]
                zmieniona = True
    return liczby

lista = [1,4,6,2,3,7,5,8]
sortowanie_bąbelkowe(lista)
print(lista, 'bąbelkowe')