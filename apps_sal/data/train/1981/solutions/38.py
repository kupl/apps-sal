class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        count = [0] * (len(nums) + 1)
        mod = 10 ** 9 + 7
                
        for r in requests:
            count[r[0]] += 1
            count[r[1]+1] -= 1
        for i in range(1, len(count)):
            count[i] += count[i-1]
                 
        res = 0
        count.sort(reverse = True)
        nums.sort(reverse = True)
        for i in range(len(count)-1): 
            res = (res + (nums[i] * count[i])) % mod
            if count[i] == 0:
                break
                
        return res

