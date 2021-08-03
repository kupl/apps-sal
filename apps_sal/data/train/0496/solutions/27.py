from collections import Counter


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        cnt, ans = Counter(A), 0

        for i in range(100000):
            if cnt[i] > 1:
                ans += cnt[i] - 1
                cnt[i + 1] += cnt[i] - 1

        return ans
