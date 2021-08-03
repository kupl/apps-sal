import string


def words_to_marks(s):
    alphabet = ' ' + string.ascii_lowercase
    s1 = 0
    for letter in s:
        s1 += alphabet.index(letter)

    return s1
