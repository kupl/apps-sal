
class Solution:
    # WA
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if W ** 2 != len(hand):
            return False
        hand.sort()
        for i in range(0, len(hand), W):
            for j in range(1, W):
                if hand[i + j] - hand[i + j - 1] != 1:
                    return False
        return True


class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        from collections import Counter
        ct = Counter(hand)
        hand = sorted(ct.items())
        # print(hand)
        i = 0
        while i < len(hand):
            if hand[i][1] == 0:
                i += 1
                continue
            hand[i] = (hand[i][0], hand[i][1] - 1)
            k = hand[i][0]
            # print(k)
            for j in range(1, W):
                k += 1
                if i + j < len(hand) and hand[i + j][0] == k:
                    # print(k)
                    hand[i + j] = (hand[i + j][0], hand[i + j][1] - 1)
                else:
                    return False
        return True
