class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if not hand or len(hand) % W != 0:
            return False
        counter = Counter(hand)
        for c in sorted(counter):
            if counter[c] > 0:
                for i in range(W)[::-1]:
                    counter[c + i] -= counter[c]
                    if counter[c + i] < 0:
                        return False
        return True
