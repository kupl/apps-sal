class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        count = Counter(hand)
        for i in range(len(hand) // W):
            (num, group_count) = (min(count.keys()), 0)
            while group_count < W:
                count[num] -= 1
                if count[num] == 0:
                    del count[num]
                elif count[num] < 0:
                    return False
                group_count += 1
                num += 1
        return True
