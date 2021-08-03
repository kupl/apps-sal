class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        counter = collections.Counter(hand)
        while counter:
            num = min(counter)
            for i in range(num, num + W):
                if i not in counter:
                    return False
                elif counter[i] == 1:
                    del counter[i]
                else:
                    counter[i] -= 1

        return True
