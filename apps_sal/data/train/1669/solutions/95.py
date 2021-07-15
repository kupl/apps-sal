from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        '''
        O(n)
        '''
        counter = Counter(hand)
        count = W
        while counter:
            if count == W:
                count = 0
                val = min(counter)
            else:
                val += 1
                if not counter[val]:
                    return False                    
            counter[val] -= 1
            if not counter[val]:
                del counter[val]
            count += 1
        return count == W

