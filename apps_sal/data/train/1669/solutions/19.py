from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if(len(hand) % W != 0):
            return False
        count = Counter(hand)
        while(count):
            min_v = min(count.keys())
            for i in range(min_v, min_v+W):
                if(count[i] == 0):
                    return False
                count[i]-=1
                if(count[i] == 0):
                    del count[i]
                    
        return True
