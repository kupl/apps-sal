class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        ln = len(shifts)
        new = [sum(shifts)]
        i = 0
        while i < ln - 1:
            new.append(new[-1] - shifts[i])
            i += 1

        S = list(S)
        ans = ''
        for i, shift in enumerate(new):
            S[i] = chr(((ord(S[i]) - ord('a') + shift) % 26) + ord('a'))

        return ''.join(S)
