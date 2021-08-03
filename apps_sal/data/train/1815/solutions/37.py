import string


class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        letters = string.ascii_lowercase
        letter_to_idx = dict()
        for i, l in enumerate(letters):
            letter_to_idx[l] = i

        suffix = [sum(shifts)]
        for i in range(1, len(shifts)):
            suffix.append(suffix[-1] - shifts[i - 1])

        res = ''
        for i, c in enumerate(S):
            res += letters[(letter_to_idx[c] + suffix[i]) % 26]

        return res
