def bekeres():
    print("II/A,B,C")
    korlista = []
    kor =0
    for i in range(5):
        kor = int(input("Adj meg egy számot:"))
        korlista.append(kor)
        if kor > 120:
            return False
    print(korlista, ":", end="")
    return korlista


def elso_idos():
    lista = bekeres()
    for i in range(len(lista)):
        if lista[i] >=70:
            hely = lista[i]
            return hely


def konzolra_ir(hely):
    print("\n\tII/D,E:")
    print("	Első idős ember korának helye a listában:",hely)


def fajl_ir(szoveg):
    f =open("oreg.txt","w",encoding="utf8")
    f.write(f"II/F:\n\t Első idős ember korának helye a listában: {szoveg}")
    f.close()
