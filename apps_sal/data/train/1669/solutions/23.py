class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        import collections
        count = collections.Counter(hand)
        while count:
            num = min(count.keys())
            val = count[num]
            for j in range(W):
                if count[num + j] < val:
                    return False
                elif count[num + j] == val:
                    del count[num + j]
                else:
                    count[num + j] -= val

        return True
