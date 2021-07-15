def define_suit(card):
    return ('clubs', 'spades', 'diamonds', 'hearts')[{'C':0,'S':1,'D':2,'H':3}.get(card[-1])]
