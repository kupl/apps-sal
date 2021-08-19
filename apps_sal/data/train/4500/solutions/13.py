def define_suit(card: str) -> str:
    """ Get a suit of given card. """
    return {'c': 'clubs', 'd': 'diamonds', 'h': 'hearts', 's': 'spades'}.get(card[-1].lower())
