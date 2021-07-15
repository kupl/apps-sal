def define_suit(card):
    for k in card:
        if k=='C':
            return 'clubs'
        elif k=='D':
            return 'diamonds'
        elif k=='H':
            return 'hearts'
        elif k=='S':
            return 'spades'
