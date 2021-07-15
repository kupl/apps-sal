class Solution:
    def maxSumRangeQuery(self, nums: List[int], reqs: List[List[int]]) -> int:
        MOD = int(1e9)+7
        n = len(nums)
        weights = [0 for _ in range(n)]
        
        for x,y in reqs:
            weights[x]+=1
            if y<n-1:
                weights[y+1]-=1
        
        for i in range(1,n):
            weights[i] += weights[i-1]
        
        print(weights)
        
        weights.sort(reverse = True)
        nums.sort(reverse = True)
        ans = 0
        
        for i in range(n):
            ans += weights[i]*nums[i]
            
        return ans % MOD
            
        

