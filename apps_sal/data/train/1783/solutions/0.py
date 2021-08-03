from functools import total_ordering


@total_ordering
class PokerHand(object):
    CARDS = "AKQJT987654321"
    RANKS = {card: idx for idx, card in enumerate(CARDS)}

    def score(self, hand):
        values, suits = zip(*hand.split())
        idxs, ordered = zip(*sorted((self.RANKS[card], card) for card in values))
        is_straight = ''.join(ordered) in self.CARDS
        is_flush = len(set(suits)) == 1
        return (-2 * sum(values.count(card) for card in values) -
                13 * is_straight - 15 * is_flush, idxs)

    def __init__(self, hand):
        self.hand = hand
        self.score = min(self.score(hand), self.score(hand.replace('A', '1')))

    def __repr__(self): return self.hand
    def __eq__(self, other): return self.score == other.score
    def __lt__(self, other): return self.score < other.score
