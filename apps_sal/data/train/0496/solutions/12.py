class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        count = collections.Counter(A)
        used = []
        ans = 0
        for x in range(90001):
            if count[x] >= 2:
                used.extend([x] * (count[x] - 1))
            elif used and count[x] == 0:
                ans += x - used.pop()
        return ans
