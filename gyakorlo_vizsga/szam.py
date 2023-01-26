import random


def szam():
    print("I/A:")
    lista = []
    sz = random.randrange(1,50)
    lista.append(sz)
    print(f"\n\tA generált szám : {lista}")
    return lista


def vizsga(lista):
    print("I/B:\t")
    for i in range(len(lista)):
        if lista[i] % 5 ==0 and lista[i] % 3 ==0:
            print("\n\tA szám öttel és 3mal osztható!")
        elif lista[i] % 5 == 0:
            print("\n\t szám öttel osztható!")
        elif lista[i] % 3 ==0:
            print("\n\tA szám osztható hárommal!")


