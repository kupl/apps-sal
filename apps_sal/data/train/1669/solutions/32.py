class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        hand = sorted(hand)
        failed = False
        while hand and (not failed):
            group = [hand[0]]
            del hand[0]
            idx = 0
            while len(group) < W and idx < len(hand):
                if group[-1] + 1 == hand[idx]:
                    group.append(hand[idx])
                    del hand[idx]
                else:
                    idx += 1
            if len(group) < W:
                failed = True
        return not failed
