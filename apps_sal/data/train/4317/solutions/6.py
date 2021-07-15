deck = ['joker','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','Q♣','K♣','A♣',
                '2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','Q♦','K♦','A♦',
                '2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥','A♥',
                '2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','Q♠','K♠','A♠']

def card_game(card_1, card_2, trump):
    if card_1 == card_2:
        return "Someone cheats."
    ordinal, trumps = ["first", "second"], f"{card_1}{card_2}".count(trump)
    if "joker" in (card_1, card_2):
        winner = ordinal[card_2 == "joker"]
    elif trumps == 1:
        winner = ordinal[trump in card_2]
    elif card_1[-1] == card_2[-1]:
        winner = ordinal[deck.index(card_2) > deck.index(card_1)]
    elif trumps == 0:
        return "Let us play again."
    return f"The {winner} card won."
