class PokerHand(object):
    CARD = "23456789TJQKA"
    def __repr__(self): return str(self.hand)
    def __init__(self, hand):
        self.hand = hand
        values = ''.join(sorted(hand[::3], key=self.CARD.index))
        suits = set(hand[1::3])
        is_straight = values in self.CARD or values == "2345A"
        is_flush = len(suits) == 1
        self.score = (2 * sum(values.count(card) for card in values)
                      + 13 * is_straight + 15 * is_flush,
                      [self.CARD.index(card) for card in values[::-1]])
        if(values == "2345A"):      
            self.score = (13 * is_straight + 15 * is_flush + 10, [3, 2, 1, 0, 12])
    def __lt__(self, other): return (self.score > other.score)
