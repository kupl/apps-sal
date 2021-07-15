class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        n = len(hand)
        if n % W != 0:
            return False
        hand.sort()
        for i in range(n // W):
            start = hand[0]
            hand.remove(start)
            for j in range(W - 1):
                if start + j + 1 in hand:
                    hand.remove(start + j + 1)
                else:
                    return False
        return True
