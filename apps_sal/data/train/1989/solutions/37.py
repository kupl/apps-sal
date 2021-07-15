def find(dp, mask):
    # d = {0:-1}
    d = {}
    ans = 0
    for i in range(0, len(dp)):
        x, y = dp[i], dp[i] ^ mask
        if y in d:
            ans = max(ans, i - d[y])
        if x not in d:
            d[x] = i
    return ans
            
class Solution:
    def longestAwesome(self, s: str) -> int:
        val = 0
        dp = [0]
        for ch in s:
            val ^= 1 << (ord(ch) - ord('0'))
            dp.append(val)
        print(dp)
        ans = find(dp, 0)
        for i in range(0, 10):
            ans = max(ans, find(dp, 1 << i))
        return ans
