def define_suit(card):
    return '{}'.format({'C':'clubs', 'S': 'spades', 'D': 'diamonds', 'H': 'hearts'}.get(card[-1]))
