class Solution:
    def longestAwesome(self, s: str) -> int:
        d = defaultdict(int)
        d[0] = -1
        
        mask = 0
        ans = 0
        for i in range(len(s)):
            curr = ord(s[i]) - ord('0')
            mask ^= 1<<curr
            if mask in d:
                ans = max(ans,i-d[mask])
            else:
                d[mask] = i
                
            for j in range(10):
                new_mask = mask^(1<<j)
                if new_mask in d:
                    ans = max(ans,i-d[new_mask])
        return ans
