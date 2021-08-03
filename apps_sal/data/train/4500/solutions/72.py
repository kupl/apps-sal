def define_suit(card):
    c = {
        'C': 'clubs',
        'D': 'diamonds',
        'H': 'hearts',
        'S': 'spades'
    }
    return c.get(card[-1])
