class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        c = Counter(hand)
        while c:
            i = min(c)
            for j in range(i, i + W):
                if not c[j]:
                    return False
                c[j] -= 1
                if not c[j]:
                    del c[j]
        return True
