class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        hand.sort()
        while hand:
            try:
                base = hand[0]
                for i in range(W):
                    hand.remove(base + i)
            except:
                return False
        return True
