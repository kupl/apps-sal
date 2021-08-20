class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        hand.sort()
        last = -1
        j = 0
        changed = False
        while hand:
            if hand[0] == last + 1 or last == -1:
                changed = False
                last = hand.pop(0)
                j += 1
                if j % W == 0:
                    last = -1
            elif not changed:
                for i in range(1, len(hand)):
                    if hand[i] <= last + 1:
                        (hand[i], hand[0]) = (hand[0], hand[i])
                    else:
                        break
                changed = True
            else:
                return False
        return True
