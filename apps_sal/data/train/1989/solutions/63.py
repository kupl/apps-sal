class Solution:
    def longestAwesome(self, s: str) -> int:
        d = collections.defaultdict(int)
        d[0]=-1
        mask = 0
        ans = 0
        for i in range(len(s)):
            mask ^= 1 << int(s[i])
            if mask in d:
                ans = max(ans, i-d[mask])
            else:
                d[mask]=i
            for j in range(10):
                tem = mask
                tem ^= 1 << j
                if tem in d:
                    ans = max(ans, i-d[tem])
        return ans
                
            
        
        
        
        
        
        
        
        
        
        

