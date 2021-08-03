class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        hand.sort()

        if len(hand) % W != 0:
            return False

        while hand:
            z = min(hand)
            for t in range(z, z + W):
                try:
                    hand.remove(t)
                except:
                    return False

        return True
