def define_suit(card):
    suits = {
        "C": "clubs",
        "D": "diamonds",
        "H": "hearts",
        "S": "spades",
    }
    last_char = card[-1]
    return suits[last_char]
