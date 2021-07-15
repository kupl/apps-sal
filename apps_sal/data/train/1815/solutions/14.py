class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        def shift(ch: str, n: int) -> str:
            print(ch, n)
            return chr((ord(ch) - ord('a') + n) % 26 + ord('a'))
        s = list(reversed(shifts))
        for i in range(1, len(s)):
            s[i] = s[i] + s[i - 1]
        res = [shift(ch, n) for ch, n in zip(S, reversed(s))]
        return \"\".join(res)
