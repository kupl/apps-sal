from collections import Counter
from copy import *


def solution(tiles):
    valid = ''
    for i in range(1, 10):
        x = tiles + str(i)
        c = Counter(x)
        if c.most_common(1)[0][1] < 5 and is_valid(Counter(x)):
            valid += str(i)
    return valid


def is_valid(hand, melds=0, pair=0):
    hand = {k: v for (k, v) in hand.items() if v}
    ordered_hand = sorted(hand, key=int)
    if melds > 5 or pair > 1:
        return False
    if len(hand) == 0:
        return True
    if hand[ordered_hand[0]] > 1:
        new_hand = deepcopy(hand)
        new_hand[ordered_hand[0]] -= 2
        if is_valid(new_hand, melds, pair + 1):
            return True
    if hand[ordered_hand[0]] > 2:
        new_hand = deepcopy(hand)
        new_hand[ordered_hand[0]] -= 3
        if is_valid(new_hand, melds + 1, pair):
            return True
    if len(ordered_hand) > 2 and int(ordered_hand[0]) + 2 == int(ordered_hand[1]) + 1 == int(ordered_hand[2]):
        new_hand = deepcopy(hand)
        new_hand[ordered_hand[0]] -= 1
        new_hand[ordered_hand[1]] -= 1
        new_hand[ordered_hand[2]] -= 1
        if is_valid(new_hand, melds + 1, pair):
            return True
    return False
