class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        ''' https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/discuss/854153/Simple-solution-Python-O(n)
            Find most requested position and calculate sum request_count * element(order of request_count) .
        '''
        mod = 10**9 + 7
        n = len(nums)
        arr = [0] * (n + 1)  # add extra element for handel n+1 case
        for i, j in requests:
            arr[i] += 1
            arr[j + 1] -= 1
        for i in range(1, n + 1):
            arr[i] += arr[i - 1]
        arr = arr[:n]  # remove the extra element
        nums.sort()
        arr.sort()
        ans = 0
        for i in range(n):
            ans += nums[i] * arr[i]
        return ans % mod
