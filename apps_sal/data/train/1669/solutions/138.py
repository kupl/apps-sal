class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        hand = sorted(hand)
        dct = {}
        for x in hand:
            if x not in dct:
                dct[x] = 1
            else:
                dct[x] += 1
        while len(hand) > 0:
            group = [hand[0]]
            check = hand[0]
            hand.remove(check)
            while len(group) < W:
                if check + 1 not in dct or dct[check + 1] < 1:
                    return False
                group.append(check + 1)
                hand.remove(check + 1)
                dct[check + 1] -= 1
                check += 1
        return True
