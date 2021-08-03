class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        count = Counter(hand)
        # min_keys = sorted(count.keys())
        for i in range(len(hand) // W):
            # base = min_keys[0]
            base = min(count)
            for num in range(base, base + W):
                count[num] -= 1
                if count[num] == 0:
                    # min_keys.remove(num)
                    del count[num]
                elif count[num] < 0:
                    return False
        return True
