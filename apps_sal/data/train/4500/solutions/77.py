def define_suit(card):
    dictionary = {'C': 'clubs', 'D': 'diamonds', 'S': 'spades', 'H': 'hearts'}

    return dictionary.get(card[-1])
