class Solution:
    def longestAwesome(self, s: str) -> int:
        prefix = {0: -1}
        curr = 0
        length = 1
        powers = [(1 << j) for j in range(10)]
        for i, c in enumerate(s):
            curr ^= 1 << int(c)
            if curr == 0:
                length = i + 1
            else:
                for p in powers:
                    length = max(length, i - prefix.get(curr ^ p, len(s)))
            if curr not in prefix:
                prefix[curr] = i
        return length
