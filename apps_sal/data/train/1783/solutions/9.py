class PokerHand(object):
    VALUES = 'A23456789TJQKA'

    def __repr__(self):
        return self.hand

    def __init__(self, hand):
        self.hand = hand
        values = ''.join(sorted(hand[::3], key=self.VALUES[1:].index))
        suits = set(hand[1::3])
        hi_straight = values in self.VALUES
        lo_straight = values[-1] + values[:-1] in self.VALUES
        is_flush = len(suits) == 1
        self.score = (2 * sum((values.count(card) for card in values)) + 13 * (hi_straight or lo_straight) + 15 * is_flush, [self.VALUES[:-1].index(card) if lo_straight else self.VALUES[1:].index(card) for card in values[::-1]])

    def __lt__(self, other):
        return other.score < self.score
