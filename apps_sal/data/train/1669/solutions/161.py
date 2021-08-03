class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        hand.sort()
        if len(hand) % W == 0:
            while len(hand) != 0:
                head = hand.pop(0)
                for i in range(1, W):
                    if head + i in hand:
                        hand.remove(head + i)
                    else:
                        return False
            return True

        else:
            return False
