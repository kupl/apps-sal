def define_suit(card):
    #     if card[-1] == "C":
    #         return "clubs"
    #     elif card[-1] == "S":
    #         return "spades"
    #     elif card[-1] == "D":
    #         return "diamonds"
    #     elif card[-1] == "H":
    #         return "hearts"
    a = {
        "C": "clubs",
        "S": "spades",
        "D": "diamonds",
        "H": "hearts"
    }
    if card[-1] in a:
        return a[card[-1]]
