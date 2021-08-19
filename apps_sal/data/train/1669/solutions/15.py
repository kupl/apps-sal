from collections import Counter


class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        c = Counter(hand)
        while len(c) > 0:
            curr = min(c)
            v = c[curr]
            del c[curr]
            for i in range(1, W):
                if curr + i not in c or c[curr + i] < v:
                    return False
                else:
                    c[curr + i] -= v
                    if c[curr + i] == 0:
                        del c[curr + i]
        return True
