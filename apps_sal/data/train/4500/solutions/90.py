def define_suit(card):
    dict_suits = {
        'C': 'clubs',
        'D': 'diamonds',
        'H': 'hearts',
        'S': 'spades',
    }

    return dict_suits[card[-1]]
