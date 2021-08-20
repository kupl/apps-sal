class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        from collections import Counter
        i = 0
        hand.sort()
        hand_count = Counter(hand)
        while i < len(hand):
            if hand[i] not in hand_count:
                i += 1
            else:
                cur = hand[i]
                for j in range(W):
                    if not hand_count[cur + j]:
                        return False
                    hand_count[cur + j] -= 1
                    if hand_count[cur + j] == 0:
                        del hand_count[cur + j]
                i += 1
        return True
