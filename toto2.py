import random

try:
    ileliczb = int(input("Podaj ilość typowanych liczb: "))
    maksliczba = int(input("Podaj maksymalną losowaną liczbę: "))
    if ileliczb > maksliczba:
        print("Błędne dane!")
        exit()
except ValueError:
    print("Błędne dane!")
    exit()

    #print("wytypuj", ileliczb,"z",maksliczba,"liczb: ")
    print("wytypuj %s z %s liczb: " % (ileliczb, maksliczba))


liczby = []

#for i in range(ileliczb)

i=0
while i < ileliczb:
    liczba = random.randint(1,maksliczba)
    if liczby.count(liczba) == 0:
        liczby.append(liczba)
        i = i +1

print("wylosowane liczby to: ", liczby)

#kontener set()

typy = set()
i = 0
while i < ileliczb:
    typ = int(input("Podaj liczbę %s: " % (i + 1)))
    if typ not in typy:
        typy.add(typ)
        i = i + 1
print(typy)


trafione = set(liczby) & typy
if trafione:
    print("\n Ilość trafień: %s" % len(trafione))
    print("Trafione liczby: ",trafione)
else:
    print("Brak trafień. Spróbuj jeszcze raz!")