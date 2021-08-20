class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        else:
            while hand != []:
                minele = min(hand)
                for i in range(0, W):
                    try:
                        hand.remove(minele + i)
                    except:
                        return False
            return True
