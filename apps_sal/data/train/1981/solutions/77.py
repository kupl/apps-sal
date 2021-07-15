class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9+7
        
        nums.sort()
        ends = sorted(requests,key=lambda x: x[1])
        starts = sorted(requests, key=lambda x: x[0])
        
        ends = [x[1] for x in ends]
        starts = [x[0] for x in starts]
        
        countends = collections.Counter([r[1] for r in requests])
        countstarts = collections.Counter([r[0] for r in requests])
        
        n = len(nums)
        counts = []
        
        #print(starts)
        #print(ends)
        for i in range(n):
            endsOnBehind = len(ends)-bisect.bisect_left(ends, i)
            startsToRight = len(starts)-bisect.bisect_right(starts, i)
            
            
            counts.append(endsOnBehind-startsToRight)
        
        #print(counts)
        counts.sort()
        
        j = n-1
        ans = 0
        
        
        for i in range(len(counts)-1, -1, -1):
            if counts[i]==0:
                break
            
            ans += counts[i]*nums[j]
            ans %= MOD
            j-=1
        
        return ans
            

