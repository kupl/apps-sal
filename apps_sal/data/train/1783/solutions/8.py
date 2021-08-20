from collections import Counter


class PokerHand(object):
    CARD = '123456789TJQKA'

    def __repr__(self):
        return self.hand

    def __init__(self, hand):
        self.hand = hand
        CARD = self.CARD
        values = ''.join(sorted(hand[::3], key=CARD.index))
        if all([c in values for c in 'A2345']):
            CARD = 'A' + self.CARD[1:-1]
            values = ''.join(sorted(hand[::3], key=CARD.index))
        is_flush = len(set(hand[1::3])) == 1
        counts = Counter(values)
        is_straight = values in CARD
        self.score = (2 * sum((counts[card] for card in values)) + 13 * is_straight + 15 * is_flush, sorted(((cnt, CARD.index(card)) for (card, cnt) in counts.most_common()))[::-1])

    def __lt__(self, other):
        return self.score > other.score
