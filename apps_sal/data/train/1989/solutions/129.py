class Solution:
    def longestAwesome(self, s: str) -> int:
        mask = 0
        pre = {0: -1}
        result = 0

        for i in range(10):
            pre[0 ^ (1 << i)] = -1

        for i, c in enumerate(s):
            n = 1 << int(c)

            mask ^= n
            if mask in pre:
                result = max(result, i - pre[mask])

            for ii in range(10):
                nmask = mask ^ (1 << ii)
                if nmask not in pre:
                    pre[nmask] = i
        return result
