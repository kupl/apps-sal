class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        freq = Counter(hand)

        while freq:
            m = min(freq)
            for i in range(m, m + W):
                v = freq[i]
                if not v:
                    return False
                if v == 1:
                    del freq[i]
                else:
                    freq[i] -= 1
        return True
