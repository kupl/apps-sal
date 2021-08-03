def define_suit(card):
    if card[1] == 'C':
        return 'clubs'
    elif card[1] == 'S':
        return 'spades'
    elif card[1] == 'D':
        return 'diamonds'
    elif card[1] == 'H':
        return 'hearts'
    elif card[1] == '0':
        if card[2] == 'C':
            return 'clubs'
        elif card[2] == 'S':
            return 'spades'
        elif card[2] == 'D':
            return 'diamonds'
        elif card[2] == 'H':
            return 'hearts'
