class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if not hand: return False
        
        hand = sorted(hand)
        queue, rs, group = [], [], []
        while hand:
            card = hand.pop(0)
            if not group or group[-1] == card - 1:
                group.append(card)
                if len(group) == W:
                    hand = queue + hand 
                    rs.append(group)
                    group, queue = [], []
            else:
                queue.append(card)
        
        if not group and not queue:
            return True 
        else:
            return False
