class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        cnt = 0
        acc_shifts = []

        for n in shifts[::-1]:
            cnt += n
            acc_shifts.append(cnt)

        acc_shifts = acc_shifts[::-1]

        new_s = []

        a_asc = ord('a')
        z_asc = ord('z')

        for i, n in enumerate(acc_shifts):
            new_ascii = ord(S[i]) + n
            new_ascii = a_asc + (new_ascii - a_asc) % 26
            new_s.append(chr(new_ascii))

        return ''.join(new_s)
