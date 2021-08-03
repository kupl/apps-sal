class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        ops = []
        for request in requests:
            ops.append((request[0], 1))
            ops.append((request[1] + 1, -1))
        ops.sort()
        nums.sort()
        counts = []
        cur = 0
        count = 0
        for idx in range(n):
            while cur < len(ops) and idx == ops[cur][0]:
                count += ops[cur][1]
                cur += 1
            counts.append(count)
        counts.sort()
        return sum([c * num for c, num in zip(counts, nums)]) % mod
