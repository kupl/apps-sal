class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        tmp = sorted([k for i, j in requests for k in [(i, 1), (j + 1, -1)]])
        counter = collections.defaultdict(int)
        last = 0
        now = 0
        for ind, delta in tmp:
            counter[now] += ind - last
            last = ind
            now += delta

        nums.sort(reverse=True)
        l = len(nums)
        result = 0
        now = 0
        for count, num in sorted(list(counter.items()), reverse=True):
            result += sum(nums[now: now + num]) * count
            now += num
            if now > l:
                break

        return result % MOD
