class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        dic = collections.OrderedDict(sorted(collections.Counter(hand).items()))
        while dic:
            m = next(iter(dic))
            for k in range(m, m + W):
                v = dic.get(k)
                if not v:
                    return False
                if v == 1:
                    del dic[k]
                else:
                    dic[k] = v - 1
        return True
