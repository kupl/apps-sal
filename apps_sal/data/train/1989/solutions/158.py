class Solution:
    def longestAwesome(self, s: str) -> int:
        
        ls = len(s)
        
        table = [-1] + [ls] * 1023
        mask = res = 0
        
        for i in range(ls):
            mask ^= 1 << int(s[i])
            
            for j in range(11):
                temp = mask
                temp ^= 1023 & (1 << j)
                res = max(res, i - table[temp])
            
            if table[mask] == ls:
                table[mask] = i
        
        
        return res
