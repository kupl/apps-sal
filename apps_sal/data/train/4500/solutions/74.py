import re
def define_suit(card):
    if re.search(r'C', card):
        return "clubs"
    elif re.search(r'D', card):
        return "diamonds"
    elif re.search(r'H', card):
        return "hearts"
    elif re.search(r'S', card):
        return "spades"
