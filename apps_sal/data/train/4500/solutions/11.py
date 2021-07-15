SUITS = 'diamonds clubs hearts spades clubs diamonds spades hearts'.split()

def define_suit(card):
    return SUITS[ord(card[-1])%7]
    

