class Solution:

    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        back_sum = [0] * len(shifts)
        N = 26
        back_sum = 0
        new_str = ''
        for i in range(len(S) - 1, -1, -1):
            back_sum += shifts[i]
            new_str += chr((ord(S[i]) - ord('a') + back_sum) % N + ord('a'))
        return new_str[::-1]
