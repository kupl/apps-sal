from collections import Counter


class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        c = Counter(A)
        ans = 0
        prev = -1
        for num in sorted(c):
            ans += max(0, prev - num + 1) * c[num] + (c[num] - 1) * c[num] // 2
            prev = num + max(0, prev - num + 1) + (c[num] - 1)
        return ans
