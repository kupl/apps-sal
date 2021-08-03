from collections import defaultdict as dd


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        nums.sort()
        n = len(nums)
        d = dd(int)
        new = [0] * n

        for r in requests:
            s, e = r
            new[s] += 1
            if e + 1 < n:
                new[e + 1] -= 1
        c = 0
        for i in range(n):

            new[i] += c
            c = new[i]

        new.sort()
        ans = 0
        for n in new[::-1]:
            ans = (ans + (n * nums[-1]) % (10**9 + 7)) % (10**9 + 7)
            nums.pop()
        return ans
