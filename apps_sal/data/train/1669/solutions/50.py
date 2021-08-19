from collections import Counter


class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        count_dict = Counter(hand)
        while count_dict:
            m = min(count_dict)
            for i in range(m, m + W):
                if i not in count_dict:
                    return False
                elif count_dict[i] == 1:
                    del count_dict[i]
                else:
                    count_dict[i] -= 1
        return True
