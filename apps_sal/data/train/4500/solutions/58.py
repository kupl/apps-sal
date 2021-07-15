def define_suit(card):
    for elem in card:
        if 'S' in card:
            return 'spades'
        elif 'D' in card:
            return 'diamonds'
        elif 'H' in card:
            return 'hearts'
        else:
            return 'clubs'
