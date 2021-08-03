import collections


class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        handCounter = Counter()
        for number in hand:
            handCounter[number] += 1
        while len(handCounter) != 0:
            m = min(handCounter.keys())
            for i in range(m, m + W):
                if i not in handCounter:
                    return False
                handCounter[i] -= 1
                if handCounter[i] == 0:
                    del handCounter[i]

        return True
