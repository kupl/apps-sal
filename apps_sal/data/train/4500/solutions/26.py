def define_suit(card):
    letter = card[-1]
    if letter == 'C':
        return 'clubs'
    elif letter == 'S':
        return 'spades'
    elif letter == 'D':
        return 'diamonds'
    else:
        return 'hearts'
