from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        
        counter = Counter(hand)
        # print (counter)
        
        while counter:
            
            key = min(counter)
            for x in range(key, key + W):
                if counter[x] < 1:
                    return False
                counter[x] -= 1
                if counter[x] == 0:
                    del counter[x]
        
        return True
