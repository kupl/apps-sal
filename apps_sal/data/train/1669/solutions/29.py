class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        counter = collections.Counter(hand)
        while counter:
            starter = min(counter.keys())
            for i in range(W):
                if starter + i not in counter:
                    return False
                else:
                    counter[starter + i] -= 1
                    if counter[starter + i] == 0:
                        del counter[starter + i]
        return True
