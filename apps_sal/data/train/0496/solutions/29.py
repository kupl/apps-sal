from collections import Counter


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        # Counting
        # If there are 2 or more values x in A, save the extra duplicated values to increment later.
        # If there are 0 values x in A, then a saved value v gets incremented to x.
        count = Counter(A)
        taken = []

        ans = 0
        for x in range(100000):
            if count[x] >= 2:
                taken.extend([x] * (count[x] - 1))
            elif taken and count[x] == 0:
                ans += x - taken.pop()

        return ans
