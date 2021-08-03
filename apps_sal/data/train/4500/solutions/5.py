def define_suit(card):
    return next(suit for suit in ['clubs', 'diamonds', 'hearts', 'spades'] if card[-1].lower() == suit[0])
