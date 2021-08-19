def define_suit(card):
    for i in card:
        if 'S' in card:
            return 'spades'
        elif 'D' in card:
            return 'diamonds'
        elif 'H' in card:
            return 'hearts'
        elif 'C' in card:
            return 'clubs'
