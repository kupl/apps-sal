# 时间复杂度：O(N * (N/W))O(N∗(N/W))，其中 NN 是 hand 的长度，(N / W)(N/W) 是 min(count) 的复杂度。
# 在 Java 中使用 TreeMap 可以将 (N / W)(N/W) 降低到 \\log NlogN。

# 空间复杂度：O(N)O(N)。
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        count = collections.Counter(hand)
        while count:
            m = min(count)
            for k in range(m, m + W):
                v = count[k]
                if not v:
                    return False
                if v == 1:
                    del count[k]
                else:
                    count[k] = v - 1

        return True
