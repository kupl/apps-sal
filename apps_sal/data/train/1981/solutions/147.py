class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        nums.sort(reverse=True)
        reqs = defaultdict(int)
        for (start, end) in requests:
            reqs[start] += 1
            reqs[end + 1] -= 1
        counts = defaultdict(int)
        h = 0
        last = -1
        for i in sorted(reqs.keys()):
            if h > 0:
                counts[h] += max(0, i - last)
            h += reqs[i]
            last = i
        res = 0
        i = 0
        n = len(nums)
        for (h, c) in sorted(list(counts.items()), reverse=True):
            for j in range(c):
                if i == n:
                    break
                num = nums[i]
                res += num * h
                res %= MOD
                i += 1
            if i == n:
                break
        return res
