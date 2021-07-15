class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        
        if len(hand) % W != 0:
            return False
        
        counter = Counter(hand)
        
        while counter:
            start = min(counter)
            
            for n in range(start, start + W):
                if n in counter:
                    counter[n] -= 1
                    if counter[n] == 0:
                        del counter[n]
                else:
                    return False
        return True

