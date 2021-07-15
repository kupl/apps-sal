from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        count = Counter(hand)
        for i in sorted(count):
            if count[i] > 0:
                for j in range(W-1, -1, -1):
                    count[i+j] -= count[i]
                    if count[i+j] < 0:
                        return False
        return True

