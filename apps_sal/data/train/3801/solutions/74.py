import string


def words_to_marks(phrase):
    sum = 0
    for letter in phrase:
        letter = string.ascii_lowercase.index(letter) + 1
        sum += letter
    return sum
