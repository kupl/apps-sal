def define_suit(card):
    a = {'C': 'clubs', 'S': 'spades', 'D': 'diamonds', 'H': 'hearts'}
    if card[-1] in a:
        return a[card[-1]]
