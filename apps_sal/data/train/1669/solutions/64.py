class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        # digits = collections.defaultdict(int)
        # for d in hand:
            # digits[d] += 1
        count = collections.Counter(hand)
        while count:
            m = min(count)
            # k, v = sorted(digits.items())[0]
            for k in range(m, m+W):
                v = count[k]
                if not v:
                    return False
                if v == 1:
                    del count[k]
                else:
                    count[k] -= 1
        return True
            
            

