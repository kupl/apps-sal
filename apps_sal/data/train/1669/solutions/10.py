class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        # counter = collections.Counter(hand)
        d = collections.defaultdict(lambda:0)
        for h in hand:
            d[h]+=1
            
        # start = min(hand)
        
        while d:
            # print(d.keys())
            start = min(d.keys())
            for i in range(start, start+W):
                if not d[i]:
                    return False
                d[i]-=1
                if not d[i]:
                    del d[i]
        
        return True
