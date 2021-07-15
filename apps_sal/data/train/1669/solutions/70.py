class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        n = len(hand)
        if n % W != 0: return False
        count = collections.Counter(hand)
        while n > 0:
            a = min(count)
            for i in range(W):
                if count[a + i] <= 0:
                    return False
                count[a + i] -= 1
                if count[a + i] == 0:
                    del count[a + i]
            n -= W
        return True
