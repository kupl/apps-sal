class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        values = [0] * (n+1)
        for i in requests:
            values[i[0]] += 1
            values[i[1]+1] -= 1
        for i in range(1, n):
            values[i] += values[i-1]
        values.sort(reverse = True)
        nums.sort(reverse = True)
        # print(values)
        ans = 0;
        mod = int(1e9) + 7;
        for i in range(n):
            ans += (values[i] * nums[i])
            ans %= mod;
        return ans
        
        
        
#         requests.sort(key = lambda x: x[0] - x[1])
#         # print(requests)
#         sz = requests[0][1] - requests[0][0] + 1
#         nums.sort(reverse = True)
#         ans = 0
#         for i in range(sz):
#             ans += nums[i]
#             ans %= mod
#         return ans;

