from collections import OrderedDict


class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if W == 1:
            return True
        if len(hand) % W:
            return False
        hand.sort()
        od = OrderedDict()
        for h in hand:
            if h in od:
                od[h] += 1
            else:
                od[h] = 1
        k = list(od.keys())[0]
        n = list(od.values())[0]
        while True:
            for i in range(W):
                if k + i in od and od[k + i] >= n:
                    od[k + i] -= n
                    if od[k + i] == 0:
                        del od[k + i]
                else:
                    return False
            if len(od) == 0:
                break
            k = list(od.keys())[0]
            n = list(od.values())[0]
        return True
