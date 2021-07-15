def define_suit(card):
    for each in card:
        if each[-1] == 'C':
            return 'clubs'
        elif each[-1] == 'D':
            return 'diamonds'
        elif each[-1] == 'H':
            return 'hearts'
        elif each[-1] == 'S':
            return 'spades'
