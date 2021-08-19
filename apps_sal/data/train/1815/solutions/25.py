class Solution:

    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        (s, ans) = ([0], [])
        for n in reversed(shifts):
            s.append((s[-1] + n) % 26)
        s = reversed(s[1:])
        for (i, c) in enumerate(S):
            n = chr((ord(c) - ord('a') + next(s)) % 26 + ord('a'))
            print(n)
            ans.append(n)
        return ''.join(ans)
