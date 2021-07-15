class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        l = len(hand)
        if l%W!=0:
            return False
        if W == 1:
            return True
        ct = Counter(hand)
        lst = sorted(list(ct.keys()))
        for l in lst:
            if l-1 not in lst and l+1 not in lst:
                return False
        while lst:
            # print(lst)
            begin = lst[0]
            ct[begin]-=1
            if ct[begin]==0:
                lst.pop(0)
            for i in range(1, W):
                if begin+i not in ct:
                    return False
                else:
                    ct[begin+i]-=1
                    if ct[begin+i]==0:
                        lst.remove(begin+i)
        return True

