dict = {'C': 'clubs',
        'S': 'spades',
        'D': 'diamonds',
        'H': 'hearts',
        }


def define_suit(card):
    return dict.get(card[-1])
