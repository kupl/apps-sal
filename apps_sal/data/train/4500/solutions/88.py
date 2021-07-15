def define_suit(card):
    card = card.lower()
    if "c" in card:
        return "clubs"
    elif "d" in card:
        return "diamonds"
    elif "h"in card:
        return "hearts"
    elif "s" in card:
        return "spades"
