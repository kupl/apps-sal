import re


def define_suit(card):
    if re.search('D\\Z', card):
        return 'diamonds'
    if re.search('C\\Z', card):
        return 'clubs'
    if re.search('H\\Z', card):
        return 'hearts'
    if re.search('S\\Z', card):
        return 'spades'
