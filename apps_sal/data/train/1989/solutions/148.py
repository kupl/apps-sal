class Solution:
    def longestAwesome(self, s: str) -> int:
        curr = 0
        longest = 0
        first = {0: -1}
        for i, c in enumerate(s):
            curr ^= 1 << int(c)
            if curr in first:
                longest = max(longest, i - first[curr])
            else:
                first[curr] = i
            mask = 1 << 9
            while mask > 0:
                if (curr ^ mask) in first:
                    longest = max(longest, i - first[curr ^ mask])
                mask >>= 1

        return longest
