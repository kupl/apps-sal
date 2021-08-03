class PokerHand(object):
    CARD = "23456789TJQKA"
    RESULT = ["Loss", "Tie", "Win"]

    def __init__(self, hand):
        values = ''.join(sorted(hand[::3], key=self.CARD.index))
        suits = set(hand[1::3])
        is_straight = values in self.CARD
        is_flush = len(suits) == 1
        self.score = (2 * sum(values.count(card) for card in values)
                      + 13 * is_straight + 15 * is_flush,
                      [self.CARD.index(card) for card in values[::-1]])

    def compare_with(self, other):
        return self.RESULT[(self.score > other.score) - (self.score < other.score) + 1]
