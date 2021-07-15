class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        hand.sort()
        dic = collections.Counter(hand)
        while dic:
            m = next(iter(dic))
            #print(m)
            for k in range(m, m+W):
                v = dic.get(k)
                #print(v,k)
                if not v: 
                    return False
                if v == 1:
                    del dic[k]
                else:
                    dic[k] = v - 1

        return True
