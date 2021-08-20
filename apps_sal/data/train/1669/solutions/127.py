from collections import Counter


class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W:
            return False
        cnt = Counter(hand)
        cards = sorted(cnt)
        while True:
            first = cards.pop()
            if not cnt[first]:
                continue
            amount = cnt[first]
            del cnt[first]
            for i in range(first - 1, first - W, -1):
                if not cnt[i]:
                    return False
                cnt[i] -= amount
                if cnt[i] < 0:
                    return False
                elif cnt[i] == 0:
                    del cnt[i]
            if not cnt:
                return True
        return False
