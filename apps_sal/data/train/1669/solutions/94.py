class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        count = collections.Counter(hand)
        while count:
            m = min(count)
            for k in range(m, m + W):
                v = count[k]
                if not v:
                    return False
                if v == 1:
                    del count[k]
                else:
                    count[k] = v - 1

        return True
