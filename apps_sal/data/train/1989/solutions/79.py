from typing import List


class Solution:
    def longestAwesome(self, s: str) -> int:
        res = 0

        pattern: List[bool] = [False] * 10

        existing = {tuple(pattern): -1}

        for cur_i, char in enumerate(s):
            num = int(char)
            pattern[num] = not pattern[num]

            for i in range(10):
                new_pattern = pattern.copy()
                new_pattern[i] = not new_pattern[i]
                res = max(res, cur_i - existing.get(tuple(new_pattern), cur_i))

            res = max(res, cur_i - existing.get(tuple(pattern), cur_i))

            existing.setdefault(tuple(pattern), cur_i)

        return res
