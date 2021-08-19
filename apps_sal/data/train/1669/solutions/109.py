class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        dic = collections.Counter(hand)
        print((dic, min(dic), dic[10]))
        while dic:
            m = min(dic)
            for num in range(m, m + W):
                if dic[num] == 0:
                    return False
                if dic[num] == 1:
                    del dic[num]
                else:
                    dic[num] = dic[num] - 1
        return True
