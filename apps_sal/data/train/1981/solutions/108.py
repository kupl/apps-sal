MODNUM = 10 ** 9 + 7


class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        N = len(nums)
        M = len(requests)
        ct = [0] * N
        requests = sorted(requests)
        (i, j) = (0, 0)
        used = []
        for k in range(N):
            while i < M and k >= requests[i][0]:
                (a, b) = requests[i]
                heappush(used, b)
                i += 1
            while len(used) > 0 and k > used[0]:
                heappop(used)
            ct[k] = len(used)
        ct = sorted(ct, reverse=True)
        nums = sorted(nums, reverse=True)
        res = 0
        for (n, c) in zip(nums, ct):
            if c == 0:
                break
            res += n * c
        return res % MODNUM
