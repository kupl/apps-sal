class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        count = collections.Counter(hand)
        while count:
            m = min(count)
            for i in range(m, m + W):
                if not count[i]:
                    return False
                if count[i] == 1:
                    del count[i]
                else:
                    count[i] -= 1
        return True
