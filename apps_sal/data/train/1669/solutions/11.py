from collections import Counter


class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        L = len(hand)
        if L % W != 0:
            return False
        count = Counter(hand)
        Nparts = L // W
        for i in range(Nparts):
            i_min = min(count.keys())
            for j in range(W):
                if i_min + j not in count:
                    return False
                count[i_min + j] -= 1
                if count[i_min + j] == 0:
                    del count[i_min + j]
        return True
