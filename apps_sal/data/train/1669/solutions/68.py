class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        hand = collections.Counter(hand)
        while True:
            if len(hand) == 0:
                return True
            m = min(hand)
            for c in range(m, m + W):
                if c not in hand:
                    return False
                if hand[c] == 1:
                    del hand[c]
                else:
                    hand[c] -= 1

