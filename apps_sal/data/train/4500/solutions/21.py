def define_suit(card):
    suits = {'C': 'clubs', 'D': 'diamonds', 'H': 'hearts', 'S': 'spades'}
    if card[-1] not in suits:
        pass
    return suits[card[-1]]
