class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        dicts = {}
        for n in hand:
            dicts[n] = dicts.get(n, 0) + 1
        while dicts:
            m = min(dicts)
            for k in range(m, m + W):
                if k not in dicts:
                    return False
                elif dicts[k] == 1:
                    del dicts[k]
                else:
                    dicts[k] -= 1
        return True
