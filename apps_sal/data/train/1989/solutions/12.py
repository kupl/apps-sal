class Solution1:
    def longestAwesome(self, s: str) -> int:
        mem = {} 
        def find_awesome(lo, hi, digit_count):
            if lo > hi:
                return 0
            if (lo, hi) in mem:
                return mem[(lo, hi)]
                    
            if digit_count & (digit_count - 1) == 0:
                return hi - lo + 1
            
            max_len = max(find_awesome(lo + 1, hi, digit_count^((1 << int(s[lo])))),
                       find_awesome(lo, hi - 1, digit_count^((1 << int(s[hi])))))
            mem[(lo, hi)] = max_len
            return max_len
        
        lo, hi, digit_count = 0, len(s) - 1, 0
        for i in range(lo, hi + 1):
            digit_count ^= (1 << int(s[i]))
        return find_awesome(lo, hi, digit_count)
    
class Solution:
    def longestAwesome(self, s: str) -> int:
        memo, state = {}, 0
        memo[state], ans = -1, 0
        for i, c in enumerate(s):            
            state ^= 1 << int(c)                        
            if state not in memo:
                memo[state] = i
            else:
                ans = max(ans, i - memo[state])                            
            for j in range(10):
                state1 = state ^ (1 << j)                                 
                if state1 in memo:
                    ans = max(ans, i - memo[state1])
        return ans
