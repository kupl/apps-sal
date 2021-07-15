class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        
        hand = sorted(hand)
        # print(hand)
        
        for split in range(len(hand) // W):
            min_val = min(hand)
            hand.remove(min_val)
            for i in range(1, W):
                if min_val + 1 not in hand:
                    return False
                else:
                    min_val += 1
                    hand.remove(min_val)
        
        return True
