class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        else:
            while hand != []:
                f = min(hand)
                for i in range(0, W):
                    try:
                        hand.remove(f + i)
                    except:
                        return False
            return True
