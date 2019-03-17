from symbol import return_stmt

__author__ = 'student'
import random

def deck():
    lista = [2,3,4,5,6,7,8,9,10,'J','D','K','A']
    kolor = ['c','d','h','s']

    wynik = list()

    for i in lista:
        for x in kolor:
            t = (i,x)
            wynik.append((t))
    return wynik


def shuffle_deck(wynik):

    random.shuffle(wynik)
    return wynik


def deal(deck, n):
    lista_win = list()
    for i in range(1,n+1):
        lista_temp = []
        for x in range(5):
            lista_temp.append(deck.pop())
        lista_win.append("Gracz: ")
        lista_win.append(i)
        lista_win.append(lista_temp)
    return lista_win

a = deck()

print(a)
print(shuffle_deck(a))
print(deal(a,5))

