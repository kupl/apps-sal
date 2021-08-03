import string


def words_to_marks(s):
    # Easy one
    letter_dict = {}
    letters = list(string.ascii_lowercase)
    for i in range(0, 26):
        letter_dict[letters[i]] = i + 1
    sum = 0
    for letter in s:
        sum += letter_dict[letter]
    return sum
