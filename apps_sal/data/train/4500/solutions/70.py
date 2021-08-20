def define_suit(card):
    d = {'C': 'clubs', 'D': 'diamonds', 'H': 'hearts', 'S': 'spades'}
    a = list(card)
    return d.get(a[-1])
