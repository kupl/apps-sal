class Solution:

    def longestAwesome(self, s: str) -> int:
        pos = {}
        open_chars = 0
        pos[open_chars] = 0
        max_len = 0
        for (i, c) in enumerate(s):
            open_chars ^= 1 << int(c)
            for j in range(-1, 10):
                if j == -1:
                    mask = 0
                else:
                    mask = 1 << j
                if open_chars ^ mask in pos:
                    max_len = max(max_len, i + 1 - pos[open_chars ^ mask])
            if open_chars not in pos:
                pos[open_chars] = i + 1
        return max_len
