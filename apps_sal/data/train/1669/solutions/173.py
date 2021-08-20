class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        sorted_hand = hand
        sorted_hand.sort()
        num_groups = int(len(hand) / W)
        for i in range(num_groups):
            num = sorted_hand[0]
            sorted_hand.remove(num)
            for j in range(W - 1):
                num += 1
                if num in sorted_hand:
                    sorted_hand.remove(num)
                else:
                    return False
        return True
