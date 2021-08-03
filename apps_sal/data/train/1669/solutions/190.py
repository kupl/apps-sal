class Solution(object):
    def isNStraightHand(self, hand, W):
        if len(hand) % W != 0:
            return False
        count = collections.Counter(hand)
        while count:
            m = min(count.keys())
            num = count[m]
            for k in range(m, m + W):
                v = count[k]
                if v < num:
                    return False
                if v == num:
                    del count[k]
                else:
                    count[k] = v - num

        return True
