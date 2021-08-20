from collections import Counter


class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        cs = Counter(hand)
        while cs:
            card = next((card for card in cs if card - 1 not in cs)) - 1
            l = -1
            while (l := (l + 1)) < W and cs[(card := (card + 1))]:
                cs[card] -= 1
                if cs[card] == 0:
                    del cs[card]
            if l != W:
                return False
        return True
