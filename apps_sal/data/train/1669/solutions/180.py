from collections import defaultdict


class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        if W == 1:
            return True

        hand.sort()
        freq = defaultdict(int)
        for c in hand:
            freq[c] += 1

        while len(freq) != 0:
            keys = list(freq.keys())
            if len(keys) < W:
                return False
            for i in range(W - 1):
                if keys[i] + 1 != keys[i + 1]:
                    return False
                freq[keys[i]] -= 1
                if freq[keys[i]] == 0:
                    freq.pop(keys[i])
                if i == W - 2:
                    freq[keys[i + 1]] -= 1
                    if freq[keys[i + 1]] == 0:
                        freq.pop(keys[i + 1])

        return True
