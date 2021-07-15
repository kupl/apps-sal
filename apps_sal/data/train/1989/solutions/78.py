class Solution:
    def longestAwesome(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        seen = {0:-1}
        max_len = 1
        p = [0] * len(s)
        for i in range(0, len(s)):
            d = ord(s[i]) - ord('0')
            p[i] = (1 << d) ^ p[i-1]
            
            if p[i] in seen:
                # If for any digit `d` we've previously seen odd instances for i' < i in s[0..i'] and
                # now we've seen odd instances of `d` in s[0..i], then there's even instances of
                # `d` in s[i'+1 .. i]; same argument for even instances of `d`. In both cases we'd
                # have even instances of every possible digit which would make a valid palindrome
                max_len = max(max_len, i - seen[p[i]])
            
            for d in range(10):
                x = p[i] | (1 << d)
                if x in seen:
                    max_len = max(max_len, i - seen[x])
                y = p[i] & (~(1 << d))
                if y in seen:
                    max_len = max(max_len, i - seen[y])
            
            if p[i] not in seen:
                seen[p[i]] = i
        
        return max_len
                
                    

                

                
                
                

