def define_suit(card):
    if 'C' in card:
        return 'clubs'
    elif 'D' in card:
        return 'diamonds'
    elif 'H' in card:
        return 'hearts'
    elif 'S' in card:
        return 'spades'
    else:
        return None
