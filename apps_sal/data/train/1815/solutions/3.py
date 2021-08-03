class Solution:
    CODE_Z = ord('z')

    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        ret = ''
        self.calc_shift_times(shifts)
        for x in range(len(S)):
            ret += self.shift(S[x], shifts[x])

        return ret

    @classmethod
    def shift(cls, c, shift_times):
        ret = ord(c) + shift_times % 26
        if ret > cls.CODE_Z:
            ret -= 26

        return chr(ret)

    @staticmethod
    def calc_shift_times(shifts: List[int]):
        for x in range(-2, -(len(shifts) + 1), -1):
            shifts[x] += shifts[x + 1]
