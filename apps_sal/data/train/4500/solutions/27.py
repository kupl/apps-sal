def define_suit(card):
    return 'clubs' if card.endswith('C') == True else 'diamonds' if card.endswith('D') == True else 'hearts' if card.endswith('H') == True else 'spades'
