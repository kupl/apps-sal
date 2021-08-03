class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        counter = collections.Counter(hand)
        s = set(hand)

        while s:
            minv = min(s)
            for i in range(minv, minv + W):
                if i not in counter:
                    return False
                counter[i] -= 1
                if counter[i] == 0:
                    del counter[i]
                    s.remove(i)

        return True
