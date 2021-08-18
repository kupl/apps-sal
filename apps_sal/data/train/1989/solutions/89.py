class Solution:
    def longestAwesome(self, s: str) -> int:
        pattern = [False] * 10
        d = {tuple(pattern): -1}
        res = 0
        for i, x in enumerate(s):
            num = int(x)
            pattern[num] = not pattern[num]

            res = max(res, i - d.get(tuple(pattern), i))

            for k in range(10):
                new_pattern = pattern.copy()
                new_pattern[k] = not new_pattern[k]
                res = max(res, i - d.get(tuple(new_pattern), i))

            d.setdefault(tuple(pattern), i)
        return res
