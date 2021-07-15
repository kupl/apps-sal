def define_suit(card):
    dict = {
        'C' : 'clubs',
        'D' : 'diamonds',
        'H' : 'hearts',
        'S' : 'spades',
            }
    return dict.get(card[-1])
