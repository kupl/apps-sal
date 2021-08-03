def define_suit(card):

    what = {"C": "clubs",
            "D": "diamonds",
            "H": "hearts",
            "S": "spades"}

    for k, v in list(what.items()):
        if k in card:
            return v
