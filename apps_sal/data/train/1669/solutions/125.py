class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) < W or len(hand) % W != 0:
            return False
        d = {}
        for i in hand:
            d[i] = d.get(i, 0) + 1
        keys = sorted(list(d.keys()))
        for i in keys:
            if d[i] == 0:
                continue
            while d[i] > 0:
                for j in range(i, i + W):
                    if j not in keys or d[j] <= 0:
                        return False
                    else:
                        d[j] = d[j] - 1
        return True
