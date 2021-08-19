class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:

        if len(hand) % W != 0:
            return False

        while(hand != []):
            minele = min(hand)
            for i in range(0, W):
                try:
                    # print(minele+i)
                    hand.remove(minele + i)
                except:
                    return False
        return True
