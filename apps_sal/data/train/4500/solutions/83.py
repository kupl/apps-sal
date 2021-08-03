def define_suit(card):
    if card[len(card) - 1] == 'S':
        return 'spades'
    elif card[len(card) - 1] == 'C':
        return 'clubs'
    elif card[len(card) - 1] == 'D':
        return 'diamonds'
    else:
        return 'hearts'
