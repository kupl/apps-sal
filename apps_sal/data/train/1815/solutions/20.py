class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        n = len(shifts)
        ss = [0] * n
        ss[-1] = shifts[-1] % 26
        for i in range(n - 2, -1, -1):
            ss[i] = (shifts[i] + ss[i + 1]) % 26

        final_chars = [None] * n
        for i, ch in enumerate(S):
            _ord = ord(ch) + ss[i]
            if _ord > 122:
                _ord -= 26
            final_chars[i] = chr(_ord)

        return ''.join(final_chars)
