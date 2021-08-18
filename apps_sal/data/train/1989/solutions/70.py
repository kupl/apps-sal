class Solution:
    def longestAwesome(self, s: str) -> int:
        pattern = 0
        d = {pattern: -1}
        res = 0
        for cur_i, x in enumerate(s):

            pattern ^= 1 << int(x)

            for i in range(10):
                new_pattern = pattern ^ (1 << i)
                res = max(res, cur_i - d.get(new_pattern, cur_i))

            res = max(res, cur_i - d.get(pattern, cur_i))

            d.setdefault(pattern, cur_i)
        return res
