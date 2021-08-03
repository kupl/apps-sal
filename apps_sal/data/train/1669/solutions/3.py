from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        count = Counter(hand)
        while count:
            key = min(count)
            for k in range(key, key + W):
                check = count[k]
                if not check:
                    return False
                else:
                    count[k] -= 1
                if check == 1:
                    del count[k]
        return True
