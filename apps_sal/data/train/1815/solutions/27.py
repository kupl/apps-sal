class Solution:

    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        S_lst = list(S)
        plus = 0
        for i in range(len(shifts) - 1, -1, -1):
            plus += shifts[i]
            temp = ord(S_lst[i]) + plus % 26
            if temp > ord('z'):
                temp = temp % (ord('z') + 1) + ord('a')
            S_lst[i] = chr(temp)
        return ''.join(S_lst)
