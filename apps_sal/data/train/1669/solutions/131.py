from collections import Counter, deque


class Solution:
    def isNStraightHand(self, hand, W):
        cnts = Counter(hand)
        for num in sorted(cnts):

            tmp = cnts[num]
            if tmp > 0:
                for j in range(num, num + W):
                    cnts[j] -= tmp
                    if cnts[j] < 0:
                        return False
        return True
