from collections import Counter


class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        n = len(hand)
        if n % W != 0:
            return False
        occurmap = Counter(hand)
        tots = 0
        hand.sort()
        for i in range(n):
            v = hand[i]
            if occurmap[v - 1] > 0 or occurmap[v] <= 0:
                continue
            count = 1
            occurmap[v] -= 1
            while count < W and occurmap[v + 1] > 0:
                count += 1
                occurmap[v + 1] -= 1
                v = v + 1
            if count == W:
                tots += 1
        if tots * W == n:
            return True
        return False
