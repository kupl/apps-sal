class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        from collections import Counter
        c = Counter(sorted(hand))
        for i in c:
            if c[i] == 0:
                continue
            for j in range(1, W):
                if c[i + j] >= c[i]:
                    c[i + j] -= c[i]
                else:
                    return False
            c[i] -= c[i]
        return True
