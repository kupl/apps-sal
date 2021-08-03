class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        hand.sort()
        if len(hand) % W != 0:
            return False

        else:
            for i in range(len(hand) // W):
                tmp = hand.pop(0)
                for j in range(W - 1):
                    if tmp + j + 1 in hand:
                        hand.pop(hand.index(tmp + j + 1))
                    else:
                        return False
            print(hand)
            if len(hand) == 0:
                return True
            else:
                return False
