from typing import List


# Aug 15, 2020
# 44 / 153 test cases passed.
# 129 / 153 test cases passed.
class Solution:
    def longestAwesome(self, s: str) -> int:
        res = 0

        # pattern[i] True means we have even number of i so far
        # pattern[i] false means we have odd number of i so far
        pattern: List[bool] = [False] * 10

        existing = {tuple(pattern): -1}

        for cur_i, char in enumerate(s):
            num = int(char)
            pattern[num] = not pattern[num]

            for i in range(10):
                new_pattern = pattern.copy()
                new_pattern[i] = not new_pattern[i]
                # existing.get(tuple(new_pattern)) give us the position of j where
                # starting from j we know we have 1 odd `num`
                res = max(res, cur_i - existing.get(tuple(new_pattern), cur_i))

            # If we have `pattern` in `existing`, then we know it is also a palindrome starting from j
            res = max(res, cur_i - existing.get(tuple(pattern), cur_i))

            if tuple(pattern) not in existing:
                existing.setdefault(tuple(pattern), cur_i)

        return res
