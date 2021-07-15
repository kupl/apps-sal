def define_suit(card):
    return ['clubs', 'spades', 'diamonds', 'hearts'][('S' in card) + 2 * ('D' in card) + 3 * ('H' in card)]
