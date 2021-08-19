class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        n = len(hand)
        if n % W != 0:
            return False
        c = collections.Counter(hand)
        while c:
            k = min(c)
            v = c[k]
            del c[k]
            for i in range(1, W):
                if c[k + i] < v:
                    return False
                else:
                    c[k + i] -= v
                    if c[k + i] == 0:
                        del c[k + i]
        return True
