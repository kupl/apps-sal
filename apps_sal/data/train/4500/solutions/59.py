def define_suit(card):
    if card[-1] == 'C':
        return 'clubs'
    if card[-1] == 'D':
        return 'diamonds'
    if card[-1] == 'H':
        return 'hearts'
    if card[-1] == 'S':
        return 'spades'
    return ''
