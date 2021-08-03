class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        l = len(shifts)
        s = list(S)[:l]
        a = ord('a')

        # [1 + 3 + 5 + 7, 3 + 5 + 7, 5 + 7, 7]
        for i in range(1, len(shifts)):
            shifts[l - 1 - i] += shifts[l - i]

        print(shifts)

        for i in range(len(shifts)):
            # (ord(s[i]) - a + shifts[i]) % 26 이렇게 바꾼 숫자를 a에 더해줌
            s[i] = chr((ord(s[i]) - a + shifts[i]) % 26 + a)

        return ''.join(s)
