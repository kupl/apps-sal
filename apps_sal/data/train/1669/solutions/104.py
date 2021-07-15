class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        l=len(hand)
        if l%W!=0:
            return False
        d=collections.Counter(hand)
        while d:
            num=min(d)
            j=1
            while num+1 in d and j!=W:
                j+=1
                num=num+1
            if j==W:
                num=min(d)
                for k in range(W):
                    if d[num]==1:
                        del d[num]
                    else:
                        d[num]-=1
                    num+=1
            else:
                return False
        return True

