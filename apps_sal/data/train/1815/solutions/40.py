class Solution:

    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        char = 'abcdefghijklmnopqrstuvwxyz'
        s = 0
        res = []
        for i in range(len(shifts) - 1, -1, -1):
            s += shifts[i]
            res.insert(0, char[(char.index(S[i]) + s) % 26])
        return ''.join(res)
