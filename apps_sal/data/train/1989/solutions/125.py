class Solution:
    def longestAwesome(self, s: str) -> int:

        seen = [len(s)] * (1 << 10)
        seen[0] = -1
        mask = 0
        res = 0

        for i, char in enumerate(s):

            mask ^= (1 << int(char))

            # Check if exact mask has been seen before
            res = max(res, i - seen[mask])

            # Check if mask (off by one digit) has been seen before
            for j in range(10):
                temp = (1 << j) ^ mask
                res = max(res, i - seen[temp])

            seen[mask] = min(seen[mask], i)

        return res
