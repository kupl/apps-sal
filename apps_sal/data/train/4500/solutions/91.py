def define_suit(card):
    suite = {
        'C': 'clubs',
        'D': 'diamonds',
        'H': 'hearts',
        'S': 'spades'
    }
    return suite[card[-1]]
