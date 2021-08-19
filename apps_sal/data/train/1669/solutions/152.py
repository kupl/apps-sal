class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        i = 0
        hand.sort()
        while hand:
            for j in range(1, W):
                if hand[i] + j not in hand:
                    return False
                hand.pop(hand.index(hand[i] + j))
            hand.pop(i)
        return True
