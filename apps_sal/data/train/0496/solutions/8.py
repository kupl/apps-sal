class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0
        min_num = min(A)
        max_num = max(A)
        count = collections.Counter(A)
        taken = []
        ans = 0
        for x in range(100000):
            if x > max_num and (not taken):
                break
            if count[x] >= 2:
                taken = taken + [x] * (count[x] - 1)
            elif taken and count[x] == 0:
                ans += x - taken.pop()
        return ans
