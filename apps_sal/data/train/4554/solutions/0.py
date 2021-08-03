from collections import Counter


def play_if_enough(hand, play):
    h = Counter(hand)
    p = Counter(play)
    if p & h == p:
        h.subtract(p)
        return (True, "".join(h.elements()))
    return (False, hand)
