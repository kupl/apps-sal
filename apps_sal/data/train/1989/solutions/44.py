class Solution:
    def longestAwesome(self, s: str) -> int:
        pos = {}
        
        def f(c):
            return ord(c) - ord('0')
        
        mask, ans = 0, 1
        pos[0] = -1
        
        for n, ch in enumerate(s):
            p = f(ch)
            mask ^= (1 << p)
            # print(\"{0:b}\".format(mask), mask)
            # even check
            if mask in pos:
                len = n - pos[mask]
                if len % 2 == 0:
                    ans = max(ans, len)
            
            # odd check
            for nn in range(10):
                nmask = mask ^ (1 << nn)
                if nmask in pos:
                    len = n - pos[nmask]
                    if len % 2 == 1:
                        ans = max(ans, len)
            
            if mask not in pos:
                pos[mask] = n
        
        return ans
