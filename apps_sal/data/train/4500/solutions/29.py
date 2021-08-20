def define_suit(card):
    suite = card[-1]
    if card[-1] == 'S':
        return 'spades'
    elif card[-1] == 'D':
        return 'diamonds'
    elif card[-1] == 'H':
        return 'hearts'
    else:
        return 'clubs'
