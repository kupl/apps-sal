class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        N = len(hand)
        if N % W != 0:
            return False
        counts = collections.Counter(hand)
        while counts:
            card = min(counts.keys())
            for _ in range(W):
                if card not in counts:
                    return False
                counts[card] -= 1
                if counts[card] == 0:
                    del counts[card]
                card += 1
        return True
