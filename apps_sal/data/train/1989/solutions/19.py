class Solution:
    def longestAwesome(self, s: str) -> int:
        memo, state = {}, 0
        memo[state], ans = -1, 0
        for i, c in enumerate(s):            
            state ^= 1 << int(c)                        
            if state not in memo: memo[state] = i
            else: ans = max(ans, i - memo[state])                            
            for n in range(10):
                state1 = state ^ (1 << n)                                 
                if state1 in memo: ans = max(ans, i - memo[state1])
        return ans  
