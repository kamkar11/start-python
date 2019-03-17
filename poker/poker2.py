from random import shuffle


def hand_rank(hand):
    # temp overwrite do sprawdzenia czy poker królewski działa
    # hand = [('A', 's'), ('K', 's'), ('D', 's'), ('J', 's'), ('10', 's')]

    # TODO: pobierz liste rang kart gracza. Uzyj listy skladanej.
    hand_rank_list = []
    for card in hand:
        hand_rank_list.append(card[0])
    # TODO: pobierz liste kolorow kart gracza. Uzyj listy skladanej.
    hand_color_list = []
    for card in hand:
        hand_color_list.append(card[1])

    print(hand_rank_list)
    print(hand_color_list)
    # histogramy rang kart graczy  okresla ile razy wystapila karta o tej samej randze,
    # potrzebne do ustalenia ukladu kart
    # TODO: uzyj funkcji 'histogram' z poprzedniego laboratorium!
    hand_rank_histogram = histogram(" ".join(hand_rank_list))
    # histogramy kolorow kart graczy, jesli 5 in hand_color_histogram.values() == True
    # to wszystkie karty sa jednego koloru
    hand_color_histogram = histogram(" ".join(hand_color_list))

    print(hand_rank_histogram)
    print(hand_color_histogram)
    # czy karty sa "po kolei" (konieczne w: poker krolewski, pokerze, strit)
    # TODO: zaimplementuj funkcje is_rank_sequence(hand) ktora zwraca True jesli karty sa po kolei
    #       w przeciwnym razie zwraca false. Pobiera liste kart jako parametr
    is_hand_rank_sequence = is_rank_sequence(hand)

    print(hand_rank_histogram.values())

    # is_hand_rank_sequence = True
    # hand_rank_histogram = ['10', 'J', 'D', 'K', 'A']
    # hand_color_histogram = ['s', 's', 's', 's', 's']

    hand_strength = 0  # zwracana zmienna, ja trzeba ustawic
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


def histogram(text):
    dictonary = {}
    text = text.replace(" ", "")
    for element in text:
        dictonary[element] = text.count(element)
    return dictonary


def deck():
    figures = ['2', '3', '4', '5', '6', '7',
               '8', '9', '10', 'J', 'D', 'K', 'A']
    colors = ['c', 'd', 'h', 's']
    complete_deck = []
    for color in colors:
        for figure in figures:
            complete_deck.append((figure, color))
    return complete_deck


def shuffle_deck(deck):
    shuffle(deck)
    return deck


def deal(deck, players_number):
    game_decks = []
    temp_all_deck = list(deck)
    for player in range(1, players_number+1):
        temp_deck = []
        for i in range(1, 5):
            for card in deck:
                if card in temp_all_deck and not card in temp_deck and len(temp_deck) < 5:
                    temp_deck.append(card)
                    temp_all_deck.remove(card)
        game_decks.append(temp_deck)

    return game_decks


deck = deck()
# print("DECK RESULT: ")
# print(deck)

shuffled_deck = shuffle_deck(deck)
# print("SHUFFLED DECK RESULT: ")
# print(shuffled_deck)

players_number = 2
game_decks = deal(shuffled_deck, players_number)
print("GAME DECKS RESULT: ")
print(game_decks)

print("COUNTING GAME DECKS STRENGTH")
for game_deck in game_decks:
    print("GAME DECK has strength " + str(hand_rank(game_deck)))