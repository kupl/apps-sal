def define_suit(card):
    if "D" in card:
        return "diamonds"
    elif "S" in card:
        return "spades"
    elif "C" in card:
        return "clubs"
    else:
        return "hearts"
