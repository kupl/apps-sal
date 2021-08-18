class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:

        counter = collections.Counter(hand)

        while counter:
            m = min(counter)
            for k in range(m, m + W):

                if not counter[k]:
                    return False

                counter[k] -= 1

                if counter[k] == 0:
                    del counter[k]
        return True
