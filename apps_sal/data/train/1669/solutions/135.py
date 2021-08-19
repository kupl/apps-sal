class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        hand.sort()
        while hand:
            curr = hand[0]
            try:
                for i in range(W):
                    hand.remove(curr)
                    curr += 1
            except:
                return False
        return True
