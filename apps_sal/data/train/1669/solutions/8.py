class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        cnt = collections.Counter(hand)
        while cnt:
            m = min(cnt)
            for i in range(m, m + W):
                if i not in cnt:
                    return False
                elif cnt[i] == 1:
                    del cnt[i]
                else:
                    cnt[i] -= 1
        return True
