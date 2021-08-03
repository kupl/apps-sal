def shift_char(char, num):

    idx = ord(char) - ord('a')
    idx = idx + num
    idx %= 26

    return chr(ord('a') + idx)


class Solution:

    def shiftingLetters(self, S: str, shifts: List[int]) -> str:

        res = list(S)

        for i in range(len(shifts) - 2, -1, -1):
            shifts[i] += shifts[i + 1]

        for i in range(len(S)):
            res[i] = shift_char(res[i], shifts[i])

        return ''.join(res)
