import re


def define_suit(card):
    if re.search('C', card):
        return 'clubs'
    elif re.search('D', card):
        return 'diamonds'
    elif re.search('H', card):
        return 'hearts'
    elif re.search('S', card):
        return 'spades'
