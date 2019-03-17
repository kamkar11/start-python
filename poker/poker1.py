from random import shuffle


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
print("DECK RESULT: ")
print(deck)

shuffled_deck = shuffle_deck(deck)
print("SHUFFLED DECK RESULT: ")
print(shuffled_deck)

players_number = 2
game_decks = deal(shuffled_deck, players_number)
print("GAME DECKS RESULT: ")
print(game_decks)