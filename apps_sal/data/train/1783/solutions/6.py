from itertools import groupby
from enum import IntEnum, auto


class PokerHand:
    def __init__(self, hand):
        self.hand = hand
        cards = hand.split()
        values = tuple(sorted(cardval.get(c[0]) or int(c[0]) for c in cards))
        groups = tuple(sorted((len(tuple(g)) for _, g in groupby(values)), reverse=True))
        hand_value = hv_table.get(groups)
        if hand_value is None:
            flush = len(set(c[1] for c in cards)) == 1
            straight = set(a - b for (a, b) in zip(values[1:], values[:-1])) == {1} or values == (2, 3, 4, 5, 14)
            if straight and flush:
                hand_value = HV.royal_flush if values[0] == 10 else HV.straight_flush
            elif flush:
                hand_value = HV.flush
            elif straight:
                hand_value = HV.straight
            else:
                hand_value = HV.highcard
        self.hand_value = hand_value

    def __lt__(lhs, rhs):
        return lhs.hand_value > rhs.hand_value

    def __eq__(lhs, rhs):
        return lhs.hand_value == rhs.hand_value

    def __repr__(self):
        return self.hand


cardval = dict(T=10, J=11, Q=12, K=13, A=14)


class HV(IntEnum):
    highcard = auto()
    pair = auto()
    two_pairs = auto()
    three_ok_a_kind = auto()
    straight = auto()
    flush = auto()
    full_house = auto()
    four_of_a_kind = auto()
    straight_flush = auto()
    royal_flush = auto()


hv_table = {
    (2, 1, 1, 1): HV.pair,
    (2, 2, 1): HV.two_pairs,
    (3, 1, 1): HV.three_ok_a_kind,
    (3, 2): HV.full_house,
    (4, 1): HV.four_of_a_kind,
}
