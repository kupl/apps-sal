def define_suit(card):
    if card[-1] == 'C':
        return 'clubs'
    elif card[-1] == 'S':
        return 'spades'
    elif card[-1] == 'H':
        return 'hearts'
    else:
        return 'diamonds'
