def define_suit(card):
    a = {"C": "clubs", "D": "diamonds", "H": "hearts", "S": "spades"}
    return a[card[-1]] if card[-1] in a else False
