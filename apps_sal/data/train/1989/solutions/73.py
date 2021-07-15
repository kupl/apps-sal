class Solution:
    def longestAwesome(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        max_len = 1
        # p[i] contains a 10-bit number where the k-th bit of p[i] is 0 if there are
        # even instances of digit k in s[0..i], or k-th bit of p[i] is 1 if there are
        # odd instances of digit k in s[0..i].
        p = [0] * len(s)
        # seen[x] holds the smallest index at which some p[i] == x was seen. We can therefore
        # query `seen` to find out when some odd/evenness digit instance state was first seen.
        # For convinience, we can say we've seen even instances of all digits [0-9] at index
        # -1, ie. we've seen zero instances of every digit before index 0
        seen = {0:-1}
        for i in range(0, len(s)):
            d = ord(s[i]) - ord('0')
            p[i] = (1 << d) ^ p[i-1]
            
            #if p[i] in seen:
                # If for any digit `d` we've previously seen odd instances for i' < i in s[0..i'] and
                # now we've seen odd instances of `d` in s[0..i], then there's even instances of
                # `d` in s[i'+1 .. i]; same argument for even instances of `d`. In both cases we'd
                # have even instances of every possible digit which would make a valid palindrome
            #    max_len = max(max_len, i - seen[p[i]])
            
            for od in range(10):
                # If we designate only one digit as the digit that could have odd instances, then
                # if we've had odd instances previously for the same digit, AND same odd/even 
                # instances for all other digits, we can make a valid palindrome.
                x = p[i] | (1 << od)
                if x in seen:
                    max_len = max(max_len, i - seen[x])
                y = p[i] & (~(1 << od))
                if y in seen:
                    max_len = max(max_len, i - seen[y])
            
            if p[i] not in seen:
                seen[p[i]] = i
        
        return max_len
                
                    

                

                
                
                

