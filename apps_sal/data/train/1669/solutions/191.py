class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:

        counter = collections.Counter(hand)

        while counter:
            m = min(counter)
            for k in range(m, m + W):
                v = counter[k]
                if not v:
                    return False
                if v == 1:
                    del counter[k]
                else:
                    counter[k] = v - 1
        return True
