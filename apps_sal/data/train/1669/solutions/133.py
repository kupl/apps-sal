from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        cards = Counter(hand)
        for card in sorted(hand):
            if cards[card] > 0:
                for i in range(W):
                    if card + i not in cards or cards[card + i] == 0:
                        return False
                    cards[card + i] -= 1
        return True
