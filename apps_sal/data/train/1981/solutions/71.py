class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        arr = [0]*(len(nums)+1)
        for i, j in requests:
            arr[i]  += 1
            arr[j+1] -= 1
        for i in range(1, len(nums)+1):
            arr[i] += arr[i-1]
        arr=arr[:len(nums)]
        arr.sort()
        nums.sort()
        s=0
        for i in range(len(arr)):
            s+=nums[i]*arr[i]
        return s%(10**9 + 7)
