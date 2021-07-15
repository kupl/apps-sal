def define_suit(card):
    suits = {
    'C' : 'clubs',
    'D' : 'diamonds',
    'S' : 'spades',
    'H' : 'hearts'
    }
    
    return suits.get(card[-1])
