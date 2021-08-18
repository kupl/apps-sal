class Solution:
    def longestAwesome(self, s: str) -> int:
        F = {0: 0}
        res = 0
        mask = 0
        j = 0

        for c in s:
            j += 1
            mask ^= 1 << ord(c) - ord('0')
            for i in range(0, 10):
                new_mask = mask ^ (1 << i)
                if new_mask in list(F.keys()):
                    res = max(res, j - F[new_mask])
                    if not mask:
                        res = max(res, j)

            if mask not in list(F.keys()):
                F[mask] = j
        return res
