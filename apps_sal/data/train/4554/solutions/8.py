from collections import Counter


def play_if_enough(hand, play):
    c1, c2 = Counter(hand), Counter(play)
    if all(c1[x] >= c2[x] for x in c2):
        return True, ''.join(x * (c1[x] - c2[x]) for x in c1)
    else:
        return False, hand
