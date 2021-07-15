class Solution:
    def longestAwesome(self, s: str) -> int:
        # n = len(s)
        # length = n
        # while length > 1:
        #     # exam medium
        #     start = 0
        #     end = start + length
        #     check = 0
        #     while end <= n:
        #         sub_s = s[start:end]
        #         tmp = {}
        #         for char in sub_s:
        #             if char not in tmp:
        #                 tmp[char] = 1
        #             else:
        #                 tmp[char] += 1 
        #         value = [a for a in list(tmp.values()) if a%2==1]
        #         if len(value) <= 1:
        #             check = 1
        #             break
        #         start += 1
        #         end += 1
        #     if check == 1:
        #         return length
        #     else:
        #         length -= 1
        # return 1
        n = len(s)
        ans, mask = 0, 0
        
        memo = [n] * 1024
        memo[0] = -1
        
        for i in range(n):
            mask ^= 1 << int(s[i])
\t\t\t
\t\t\t# Case 1. Check if we have seen similar mask
            ans = max(ans, i - memo[mask])
            
\t\t\t# Case 2. Check for masks that differ by one bit
            for j in range(10):
                test_mask = mask ^ (1 << j)
                ans = max(ans, i - memo[test_mask])
                
\t\t\t# save the earliest position
            memo[mask] = min(memo[mask], i)    
        
        return ans
        
