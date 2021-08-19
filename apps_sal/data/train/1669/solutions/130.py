class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        hand.sort()
        while len(hand) > 0:
            val = hand.pop(0)
            for j in range(W - 1):
                try:
                    val += 1
                    indx = hand.index(val)
                    hand.pop(indx)
                except:
                    return False
        return True
