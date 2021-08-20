class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        hand.sort()
        length = len(hand)
        count = 0
        group = []
        while 1:
            for i in range(W - 1):
                if hand[0] + i + 1 in hand:
                    count += 1
                    hand.pop(hand.index(hand[0] + i + 1))
                else:
                    return False
            hand.pop(0)
            if len(hand) == 0:
                return True
