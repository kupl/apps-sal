class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        f = 80001 * [0]
        max_ = -1
        for i in A:
            f[i] += 1
            max_ = max(max_, i)
        hold = []
        res = 0
        for i in range(max_ + len(A) + 1):
            if hold and f[i] == 0:
                res += i - hold.pop()
            elif f[i] > 1:
                hold = (f[i] - 1) * [i] + hold
        return res
