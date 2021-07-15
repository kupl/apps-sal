from collections import Counter

def play_if_enough(hand, play):
    available = Counter(hand)
    available.subtract(Counter(play))
    if min(available.values()) < 0:
        return (False, hand)
    return (True, "".join(available.elements()))
