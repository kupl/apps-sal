class Solution:
    def longestAwesome(self, s: str) -> int:
        seen = {0: -1}
        mask = 2 ** 10 - 1
        bs = [0] + [(1 << i) for i in range(10)]
        cur = 0
        best = 1
        for i in range(len(s)):
            b = 1 << int(s[i])
            cur = (cur ^ b) & mask
            for m in bs:
                if cur ^ m in seen:
                    best = max(best, i - seen[cur ^ m])
            if cur not in seen:
                seen[cur] = i
        print(seen)
        print(bs)
        return best
