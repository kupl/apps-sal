class PokerHand():
    
    def __init__(self, hand):
        hand = hand.split()
        # get card values
        values = sorted('__23456789TJQKA'.index(card[0]) for card in hand)[::-1]
        # check if same suit
        same_suit = len({card[1] for card in hand}) == 1
        # check if straight
        straight = [values[0]-i for i in range(5)] == values
        # check n of a kind
        kinds = {i: [] for i in range(1, 5)}
        for value in sorted(set(values))[::-1]:
            how_many = values.count(value)
            kinds[how_many].append(value)
        
        # calculate rank
        if same_suit and straight:    self.rank = 8, values                # royal/straight flush
        elif kinds[4]:                self.rank = 7, kinds[4], kinds[1]    # four of a kind
        elif kinds[3] and kinds[2]:   self.rank = 6, kinds[3], kinds[2]    # full house
        elif same_suit:               self.rank = 5, values                # flush
        elif straight:                self.rank = 4, values                # straight
        elif kinds[3]:                self.rank = 3, kinds[3], kinds[1]    # three of a kind
        elif len(kinds[2]) == 2:      self.rank = 2, kinds[2], kinds[1]    # two pairs
        elif kinds[2]:                self.rank = 1, kinds[2], kinds[1]    # one pair
        else:                         self.rank = 0, values                # high card
    
    def compare_with(self, other):
        return ( "Win"  if self.rank > other.rank else
                 "Loss" if self.rank < other.rank else
                 "Tie" )
