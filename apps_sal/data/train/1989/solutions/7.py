class Solution:
    def longestAwesome(self, s: str) -> int:
        pos = {0: -1}
        bitmask = 0
        ans = 0
        n = len(s)
        for i in range(n):
            bitmask ^= (1 << int(s[i]))
            for j in range(10):
                if bitmask ^ (1 << j) in pos:
                    ans = max(ans, i - pos[bitmask ^ (1 << j)])
            if bitmask in pos:
                ans = max(ans, i - pos[bitmask])
            else:
                pos[bitmask] = i

        return ans
