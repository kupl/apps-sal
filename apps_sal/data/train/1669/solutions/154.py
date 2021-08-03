class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        hand.sort()
        while hand:
            start = hand[0]
            hand.remove(start)
            for i in range(W - 1):
                start += 1
                if start in hand:
                    hand.remove(start)
                else:
                    return False
        return len(hand) == 0
