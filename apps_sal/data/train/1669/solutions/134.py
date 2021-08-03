class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) == 0:
            return False
        if len(hand) % W > 0:
            return False
        count = {}
        for n in hand:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1

        total = sum(count.values())
        for n in sorted(hand):
            if total == 0:
                break
            if count[n] == 0:
                continue
            for i in range(W):
                target = n + i
                if target in count and count[target] > 0:
                    count[target] -= 1
                    total -= 1
                else:
                    return False
        return True
