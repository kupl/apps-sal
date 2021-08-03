def define_suit(card):
    ls = [char for char in card]
    if ls[-1] == 'C':
        return 'clubs'
    elif ls[-1] == 'D':
        return 'diamonds'
    elif ls[-1] == 'H':
        return 'hearts'
    else:
        return 'spades'
