def bubble_up(liczby):
    num = liczby[1]
    ind = liczby[0]
    n = len(num)
    zmieniona = True
    while zmieniona == True:
        zmieniona = False
        for i in range(n-1):
            if num[i] < num[i+1]:
                num[i], num[i+1] = num[i+1],num[i]
                ind[i], ind[i + 1] = ind[i + 1], ind[i]
                zmieniona = True
    return num,ind

def Insertion_up(liczby):
    num = liczby[1]
    ind = liczby[0]
    n = len(num)
    for i in range(1,n):
        wstawianie = num[i]
        wst = ind[i]
        j = i - 1
        while j >= 0 and num[j] < wstawianie:
            num[j+1] = num[j]
            ind[j+1] = ind[j]
            j = j - 1
        num[j+1] = wstawianie
        ind[j+1] = wst
    return num, ind
