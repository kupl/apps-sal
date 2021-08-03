class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefSum = [0 for x in range(len(nums))]
        starts = sorted([x[0] for x in requests])
        ends = sorted([x[1] for x in requests])

        count = 0
        s = 0
        e = 0
        for i in range(len(nums)):
            while s < len(starts) and starts[s] == i:
                count += 1
                s += 1

            while e < len(ends) and ends[e] < i:
                count -= 1
                e += 1

            prefSum[i] = count

        prefSum.sort()
        nums.sort()

        res = 0
        for i in range(len(nums)):
            res += prefSum[i] * nums[i]

        mod = int(1e9 + 7)

        return res % mod
