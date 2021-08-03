def define_suit(card):
    suits = {'C': 'clubs', 'D': 'diamonds', 'S': 'spades', 'H': 'hearts'}
    if card[-1] in suits:
        return suits[card[-1]]
