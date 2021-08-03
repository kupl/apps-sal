from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        cs = Counter(hand)

        for card in hand:
            if not cs[card] or cs[(card := card - 1)]:
                continue

            l = -1
            while (l := l + 1) < W and cs[(card := card + 1)]:
                cs[card] -= 1
                if cs[card] == 0:
                    del cs[card]

            if l != W:
                return False

        return True
