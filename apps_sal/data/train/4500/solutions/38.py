def define_suit(card):
    if 'S' in card:
        return 'spades'
    elif 'C' in card:
        return 'clubs'
    elif 'H' in card:
        return 'hearts'
    else:
        return 'diamonds'
