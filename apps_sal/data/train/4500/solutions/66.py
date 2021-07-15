import re
def define_suit(card):
    if re.search(r"D\Z",card):
        return "diamonds"
    if re.search(r"C\Z",card):
        return 'clubs'
    if re.search(r"H\Z",card):
        return 'hearts'
    if re.search(r"S\Z",card):
        return 'spades'
    

