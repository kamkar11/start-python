import sys
cos = sys.argv[1:]
licznik = 0
list = []
for x in cos:
    if len(x)>=3:
        list.append(x)
        licznik=licznik+1
print(licznik)
list.reverse()
for y in list:
    sys.stdout.write(y +" ")
