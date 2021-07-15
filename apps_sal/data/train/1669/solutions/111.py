class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if(len(hand)%W != 0):
            return False
        
        data = collections.Counter(hand)
        while(data):
            m = min(data)
            for k in range(m, m+W):
                v = data[k]
                if(not v):
                    return False
                if(v == 1):
                    del data[k]
                else:
                    data[k] -= 1
        return True

