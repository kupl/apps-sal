class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:

        if (len(hand) % W) != 0:
            return False
        
        hand.sort()
        c = Counter(hand)
        
        for i in range(len(hand) // W):
            
            if len(hand) < W:
                return False
            
            keys = list(c.keys())
            key = keys[0]
            
            for j in range(W):
                if key not in c:
                    return False
                
                if c[key] == 1:
                    del c[key]
                    key += 1
                    
                else:
                    c[key] -= 1
                    key += 1
                    
        return True
