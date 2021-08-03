class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        count = collections.Counter(hand)
        while count:
            x = min(count)
            for k in range(x, x + W):
                v = count[k]
                if not v:
                    return False
                if v == 1:
                    del count[k]
                else:
                    count[k] = v - 1
        return True
