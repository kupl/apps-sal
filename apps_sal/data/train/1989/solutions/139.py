class Solution:
    def longestAwesome(self, s: str) -> int:

        d = {0: -1}
        mask = 0
        maxi = 1
        for i in range(len(s)):
            x = int(s[i])
            mask = mask ^ 1 << x

            for j in range(0, 10):
                if mask ^ 1 << j in d:
                    maxi = max(maxi, i - d[mask ^ 1 << j])

            if mask in d:
                maxi = max(maxi, i - d[mask])

            else:
                d[mask] = i

        return maxi
