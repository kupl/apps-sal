class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        hand = sorted(hand)
        counter = collections.Counter(hand)
        while counter:
            m = min(counter)
            for i in range(W):
                num = m + i
                if num in counter:
                    counter[num] -= 1
                    if counter[num] == 0: del counter[num]
                else:
                    return False
        return True
                    
                

