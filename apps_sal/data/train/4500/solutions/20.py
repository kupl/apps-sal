def define_suit(card):
    for letter in card:
        if letter.upper() == 'C':
            return 'clubs'
        elif letter.upper() == 'S':
            return 'spades'
        elif letter.upper() == 'D':
            return 'diamonds'
        elif letter.upper() == 'H':
            return 'hearts'
