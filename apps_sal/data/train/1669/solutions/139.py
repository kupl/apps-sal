from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        counter = Counter(hand)
        for key in sorted(counter):
            if counter[key] > 0:
                for i in range(1, W):
                    counter[key + i] -= counter[key]
                    if counter[key + i] < 0:
                        return False
                counter[key] = 0
        return True
