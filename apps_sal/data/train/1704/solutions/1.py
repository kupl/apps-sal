from collections import Counter


class Card(object):

    def __init__(self, card):
        if card[0] in '23456789':
            self.rank = int(card[0])
        else:
            self.rank = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}.get(card[0])
        self.suit = card[1]


class PokerHand(object):

    def __init__(self, hand):
        self.hand = [Card(card) for card in hand.split()]
        self.rank_counts = Counter((card.rank for card in self.hand))

    def compare_with(self, other):
        return 'Win' if self.score > other.score else 'Loss' if self.score < other.score else 'Tie'

    @property
    def score(self):

        def is_flush():
            return len({card.suit for card in self.hand}) == 1

        def is_straight():

            def is_sequential(arr):
                return all((a + 1 == b for (a, b) in zip(arr, arr[1:])))
            arr = sorted((card.rank for card in self.hand))
            return is_sequential(arr) or (is_sequential(arr[:4]) and arr[0] == 2 and (arr[-1] == 14))

        def is_straight_flush():
            return is_flush() and is_straight()

        def is_n_of_kind(n):
            return n in list(self.rank_counts.values())

        def is_full_house():
            return is_n_of_kind(3) and is_n_of_kind(2)

        def is_2_pair():
            return list(self.rank_counts.values()).count(2) == 2

        def get_by_count(n):
            return tuple((rank for (rank, count) in sorted(list(self.rank_counts.items()), key=lambda x: (x[1], -x[0])) if count == n))
        if is_straight_flush():
            return (9, get_by_count(1))
        elif is_n_of_kind(4):
            return (8, get_by_count(4), get_by_count(1))
        elif is_full_house():
            return (7, get_by_count(3), get_by_count(2))
        elif is_flush():
            return (6, get_by_count(1))
        elif is_straight():
            return (5, get_by_count(1))
        elif is_n_of_kind(3):
            return (4, get_by_count(3), get_by_count(1))
        elif is_2_pair():
            return (3, get_by_count(2), get_by_count(1))
        elif is_n_of_kind(2):
            return (2, get_by_count(2), get_by_count(1))
        else:
            return (1, get_by_count(1))
