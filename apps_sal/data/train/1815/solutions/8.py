import string


class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        if len(S) == 0:
            return ''

        # define alphabet mapping
        letters = string.ascii_lowercase
        num_letters = len(letters)

        # find the final positions of each letter before actually shifting
        final_shifts = [shift % num_letters for shift in shifts]

        running_shift = 0
        # start at the end so that we only have to go through list once
        for i, shift in enumerate(final_shifts[::-1]):
            index = len(final_shifts) - 1 - i
            # skip the \"last\"
            if index < len(final_shifts) - 1:
                final_shifts[index] = (final_shifts[index] + running_shift) % num_letters
                # print('running_shift {} i {} running_shift {} shift {} value {}. {}'.format(
                #     running_shift, index, running_shift, shift, final_shifts[i], final_shifts))

            # accumulate going forward
            running_shift += shift

        result = []
        for i, shift in enumerate(final_shifts):
            # find position of letter
            letter = S[i]
            # find position + shift
            position = (letters.index(letter) + shift) % num_letters
            shift_letter = letters[position]
            result.append(shift_letter)

        return ''.join(result)
