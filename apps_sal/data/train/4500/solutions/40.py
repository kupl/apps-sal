def define_suit(card):
    print(card)
    return ('clubs', 'spades', 'diamonds', 'hearts')['CSDH'.index(card[-1])]
