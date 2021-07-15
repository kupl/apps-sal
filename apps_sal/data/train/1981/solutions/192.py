class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        vals = []
        nums.sort()
        for i in range(len(nums)):
            vals.append(0)
        for request in requests:
            vals[request[0]] += 1
            if request[1] + 1 < len(nums):
                vals[request[1]+1] -= 1
        count = 0
        for i in range(len(vals)):
            vals[i] = vals[i]+count
            count = vals[i]
        vals.sort()
        index = len(nums)-1
        total = 0
        while vals[index] != 0 and index >= 0:
            total += vals[index]*nums[index]
            index -= 1
        return total%(10**9 + 7)
