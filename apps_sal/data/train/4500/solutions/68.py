def define_suit(card):
    if card[-1] == 'D':
        return 'diamonds'
    elif card[-1] == 'C':
        return 'clubs'
    elif card[-1] == 'S':
        return 'spades'
    else:
        return 'hearts'
