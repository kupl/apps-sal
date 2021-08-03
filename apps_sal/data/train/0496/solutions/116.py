from collections import Counter


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        counts = Counter(A)
        taken = []
        ans = 0

        for num in range(50001):
            num_count = counts[num]
            if num_count >= 2:
                taken.extend([num] * (num_count - 1))
            elif taken and num_count == 0:
                ans += num - taken.pop()

        return ans
