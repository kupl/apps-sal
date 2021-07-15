def define_suit(card):
    return {'C': 'clubs', 'S': 'spades', 'D': 'diamonds', 'H': 'hearts'}.setdefault(card[-1], None)
