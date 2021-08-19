class Solution:

    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        suffix_sum_shifts = []
        suffix_sum = 0
        for shift in shifts[::-1]:
            suffix_sum += shift
            suffix_sum %= 26
            suffix_sum_shifts.append(suffix_sum)
        suffix_sum_shifts = suffix_sum_shifts[::-1]
        shifted_str = ''
        for i in range(len(S)):
            new_ord = (ord(S[i]) - ord('a') + suffix_sum_shifts[i]) % 26 + ord('a')
            shifted_str += chr(new_ord)
        return shifted_str
