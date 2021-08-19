class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W:
            return False
        counter = dict()
        for h in hand:
            temp = counter.get(h, 0)
            temp += 1
            counter[h] = temp
        while counter:
            start = min(counter.keys())
            for k in range(start, start + W):
                v = counter.get(k)
                if not v:
                    return False
                if v == 1:
                    del counter[k]
                else:
                    counter[k] = v - 1
        return True
