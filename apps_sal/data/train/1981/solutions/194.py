class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        diff = [0 for i in range(n + 1)]
        for req in requests:
            diff[req[0]] += 1
            diff[req[1] + 1] -= 1
        for i in range(1, n + 1):
            diff[i] += diff[i - 1]
        diff.pop(-1)
        sort_idx = [i for i in range(n)]
        sort_idx = sorted(sort_idx, reverse=True, key=lambda x: diff[x])
        nums = sorted(nums, reverse=True)
        temp = [-1 for i in range(n)]
        for i in range(n):
            temp[sort_idx[i]] = nums[i]
        nums = temp[:]
        temp[0] = nums[0]
        ret = 0
        for i in range(1, n):
            temp[i] = temp[i - 1] + nums[i]
        for req in requests:
            if not req[0]:
                ret += temp[req[1]]
            else:
                ret += temp[req[1]] - temp[req[0] - 1]
            ret %= 1000000007
        return ret
