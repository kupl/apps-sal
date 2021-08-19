from collections import Counter


class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        dic = Counter(hand)
        while dic:
            small = min(dic.keys())
            for i in range(small, small + W):
                if dic[i] == 0:
                    return False
                dic[i] -= 1
                if dic[i] == 0:
                    del dic[i]
        return True
