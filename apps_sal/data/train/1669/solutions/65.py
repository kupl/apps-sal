class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        count = collections.Counter(hand)
        while count:
            m = min(count)
            for k in range(m, m + W):
                if not count[k]:
                    return False
                if count[k] == 1:
                    del count[k]
                else:
                    count[k] -= 1
        return True
