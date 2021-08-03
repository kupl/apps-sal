class Solution:
    def longestAwesome(self, s: str) -> int:
        n = len(s)
        a = [0 for _ in range(n)]
        for i in range(n):
            x = a[i - 1] if i > 0 else 0
            a[i] = x ^ (1 << int(s[i]))

        dp = 1
        ht = {}
        ht[a[0]] = 0

        for i in range(1, n):
            d = 1
            if a[i] == 0:
                d = i + 1
            else:
                if a[i] in ht:
                    d = max(d, i - ht[a[i]])
                for j in range(10):
                    x = a[i] ^ (1 << j)
                    if x == 0:
                        d = i + 1
                        break
                    if x in ht:
                        d = max(d, i - ht[x])

            dp = max(dp, d)
            if not a[i] in ht:
                ht[a[i]] = i

        return dp
