class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        count = collections.Counter(hand)

        while count:
            n = min(count.keys())
            n_count = count[n]
            for x in range(n + 1, n + W):
                if count[x] < n_count:
                    return False
                count[x] -= n_count
                if count[x] == 0:
                    count.pop(x)
            count.pop(n)

        return True
