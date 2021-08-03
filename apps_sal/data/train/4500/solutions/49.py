def define_suit(card):
    SUITS = ['clubs', 'diamonds', 'hearts', 'spades']
    for i in SUITS:
        if card[-1] == str.upper(i[0]):
            return i
