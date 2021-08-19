from collections import defaultdict


class Solution(object):

    def isNStraightHand(self, hand, W):
        dic = dict()
        for val in hand:
            dic[val] = dic.get(val, 0) + 1
        while dic:
            min_val = min(dic.keys())
            for i in range(min_val, min_val + W):
                v = dic.get(i, 0)
                if v == 0:
                    return False
                dic[i] -= 1
                if dic[i] == 0:
                    dic.pop(i)
        return True
