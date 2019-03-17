import random

# słownik symboli unicode
unicode_dict = {'s': '\u2660', 'h': '\u2665', 'd': '\u2666', 'c': '\u2663'}


class Card:

    def __init__(self, rank, suit):
        # TODO: definicja metody
        self.color = suit
        self.rank = rank

    def get_value(self):
        # TODO: definicja metody (ma zwracać kartę w takiej reprezentacji, jak dotychczas, tzn. krotka)
        return tuple(self.rank, self.color)

    def __str__(self):
        # TODO: definicja metody, przydatne do wypisywania karty
        # print(str(self.rank) + str(unicode_dict[self.color]))
        return str(str(self.rank) + str(unicode_dict[self.color]))


class Deck():

    def __init__(self, *args):
        # TODO: definicja metody, ma tworzyć niepotasowaną talię (jak na poprzednich lab)
        figures = ['2', '3', '4', '5', '6', '7',
                   '8', '9', '10', 'J', 'D', 'K', 'A']
        colors = ['c', 'd', 'h', 's']
        complete_deck = []
        for color in colors:
            for figure in figures:
                complete_deck.append((figure, color))
        self.deck = complete_deck

    def __str__(self):
        # TODO: definicja metody, przydatne do wypisywania karty
        cards = ""
        for card in self.deck:
            cards += str((str(card[0]) + str(unicode_dict[card[1]])) + " ")
        return cards

    def shuffle(self):
        # TODO: definicja metody, tasowanie
        random.shuffle(self.deck)

    def deal(self, players):
        # TODO: definicja metody, otrzymuje listę graczy i rozdaje im karty wywołując na nich metodę take_card z Player
        temp_all_deck = list(self.deck)
        for player in players:
            temp_deck = []
            for index in range(1, 5):
                for card in self.deck:
                    if card in temp_all_deck and not card in temp_deck and len(temp_deck) < 5:
                        temp_deck.append(card)
                        player.take_card(card)
                        temp_all_deck.remove(card)


class Player():

    def __init__(self, money, name=""):
        self.__stack_ = money
        self.__name_ = name
        self.__hand_ = []

    def take_card(self, card):
        self.__hand_.append(card)

    def get_stack_amount(self):
        return self.__stack_

    def get_player_hand_immutable(self):
        return tuple(self.__hand_)

    def cards_to_str(self):
        # TODO: definicja metody, zwraca stringa z kartami gracza
        cards = ""
        for card in self.__hand_:
            cards += str((str(card[0]) + str(unicode_dict[card[1]])) + " ")
        return cards


def histogram(text):
    dictonary = {}
    text = text.replace(" ", "")
    for element in text:
        dictonary[element] = text.count(element)
    return dictonary


# slownik wartosci kart w postaci int, dwojka - 2, ...., as - 14
card_rank_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                    "8": 8, "9": 9, "10": 10, "J": 11, "D": 12,
                    "K": 13, "A": 14}


def get_player_hand_rank(hand):
    # TODO: wstawić metodę z poprzedniego lab
    # temp overwrite do sprawdzenia czy poker królewski działa
    # hand = [('A', 's'), ('K', 's'), ('D', 's'), ('J', 's'), ('10', 's')]
    # print(hand)
    hand = list(hand)
    hand_rank_list = []
    for card in hand:
        hand_rank_list.append(card[0])

    hand_color_list = []
    for card in hand:
        hand_color_list.append(card[1])

    hand_rank_histogram = histogram(" ".join(hand_rank_list))
    hand_color_histogram = histogram(" ".join(hand_color_list))

    is_hand_rank_sequence = is_rank_sequence(hand)

    hand_strength = 0
    # ------ sprawdzamy uklad gracza 1:
    # --- sprawdzamy poker krolewski: 5 kart w tym samym kolorze, po kolei, najwyzsza to as
    if((5 in hand_color_histogram.values()) and ('A' in hand_rank_list) and is_hand_rank_sequence):
        hand_strength = 10
    # --- sprawdzamy poker: 5 kart w tym samym kolorze, po kolei
    elif((5 in hand_color_histogram.values()) and is_hand_rank_sequence):
        hand_strength = 9
    # --- sprawdzamy karete: 4 karty tej samej rangi
    elif(4 in hand_rank_histogram.values()):
        hand_strength = 8
    # --- sprawdzamy full house: 3 karty tej samej rangi i 2 karty tej samej rangi
    elif(3 in hand_rank_histogram.values() and 2 in hand_rank_histogram.values()):
        hand_strength = 7
    # --- sprawdzamy kolor
    elif(5 in hand_color_histogram.values()):
        hand_strength = 6
    # --- sprawdzamy strit
    elif(is_hand_rank_sequence and not (5 in hand_color_histogram.values())):
        hand_strength = 5
    # --- sprawdzamy trojke
    elif(3 in hand_rank_histogram.values()):
        hand_strength = 4
    # --- sprawdzamy dwie pary
    elif(list(hand_rank_histogram.values()).count(2) == 2):
        hand_strength = 3
    # --- sprawdzamy jedna pare
    elif(2 in hand_rank_histogram.values()):
        hand_strength = 2
    # --- sprawdzamy wysoka karte
    else:
        hand_strength = 1

    return(hand_strength)


def is_rank_sequence(hand):
    hand_rank_list = []
    for card in hand:
        hand_rank_list.append(card[0])
    if set(['10', 'J', 'D', 'K', 'A']).issubset(set(hand_rank_list)):
        return True
    elif set(['9', '10', 'J', 'D', 'K']).issubset(set(hand_rank_list)):
        return True
    elif set(['8', '9', '10', 'J', 'D']).issubset(set(hand_rank_list)):
        return True
    elif set(['7', '8', '9', '10', 'J']).issubset(set(hand_rank_list)):
        return True
    elif set(['6', '7', '8', '9', '10']).issubset(set(hand_rank_list)):
        return True
    elif set(['5', '6', '7', '8', '9']).issubset(set(hand_rank_list)):
        return True
    elif set(['4', '5', '6', '7', '8']).issubset(set(hand_rank_list)):
        return True
    elif set(['3', '4', '5', '6', '7']).issubset(set(hand_rank_list)):
        return True
    elif set(['2', '3', '4', '5', '6']).issubset(set(hand_rank_list)):
        return True
    else:
        return False
