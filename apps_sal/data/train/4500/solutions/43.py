def define_suit(card):
    c = card[-1]
    if c == 'C':
        return 'clubs'
    elif c == 'D':
        return 'diamonds'
    elif c == 'H':
        return 'hearts'
    else:
        return 'spades'
