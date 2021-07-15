from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        c = Counter(hand)
        while c:
            j = min(c)
            for i in range(j,j+W):
                if not c[i]:
                    return False
                if c[i] == 1:
                    del c[i]
                else:
                    c[i] -= 1
        return True

