def define_suit(card):
    # Good luck
    return 'clubs' if card[-1]=='C' \
            else 'spades' if card[-1]=='S' \
            else 'diamonds' if card[-1]=='D' \
            else 'hearts' if card[-1]=='H' \
            else None
