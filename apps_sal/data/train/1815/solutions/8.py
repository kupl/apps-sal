import string


class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        if len(S) == 0:
            return ''

        letters = string.ascii_lowercase
        num_letters = len(letters)

        final_shifts = [shift % num_letters for shift in shifts]

        running_shift = 0
        for i, shift in enumerate(final_shifts[::-1]):
            index = len(final_shifts) - 1 - i
            if index < len(final_shifts) - 1:
                final_shifts[index] = (final_shifts[index] + running_shift) % num_letters

            running_shift += shift

        result = []
        for i, shift in enumerate(final_shifts):
            letter = S[i]
            position = (letters.index(letter) + shift) % num_letters
            shift_letter = letters[position]
            result.append(shift_letter)

        return ''.join(result)
