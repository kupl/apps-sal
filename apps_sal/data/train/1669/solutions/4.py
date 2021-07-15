from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        N = len(hand)
        if N%W != 0:
            return False
                
        counter = Counter(hand)
        while counter:
            first = min(counter.keys())
            for i in range(first, first+W):
                if i not in counter:
                    return False
                counter[i] -= 1
                if counter[i] == 0:
                    del counter[i]
                    
        return True
