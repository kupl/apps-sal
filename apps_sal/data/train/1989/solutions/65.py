class Solution:

    def longestAwesome(self, s: str) -> int:
        digit = []
        for i in range(10):
            digit.append(1 << i)
        digit.append(0)
        cum = 0
        bk = [-2 for _ in range(2 ** 10 + 1)]
        bk[0] = -1
        ans = 0
        for (i, x) in enumerate(s):
            x = int(x)
            cum ^= digit[x]
            for d in digit:
                mask = cum ^ d
                if bk[mask] >= -1:
                    ans = max(ans, i - bk[mask])
            if bk[cum] == -2:
                bk[cum] = i
        return ans
