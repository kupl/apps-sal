class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # https://leetcode.com/problems/two-city-scheduling/discuss/297143/Python-faster-than-93-28-ms
        # https://leetcode.com/problems/two-city-scheduling/discuss/278944/3-ways-to-solve.
        res = 0
        costs.sort(key = lambda x: x[1]-x[0], reverse = True)
        for i in range(len(costs)//2):
            res += costs[i][0]
        for i in range(len(costs)//2, len(costs)):
            res += costs[i][1]
            
        return res
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        costs.sort(key=lambda x: (x[1]-x[0]), reverse=True)
        print (costs)
        ans=0
        half=len(costs)//2
        for i in range(half):
            ans+= costs[i][0]
        for i in range(half,len(costs)):
            ans+=costs[i][1]
        return ans
            
        

