import string
def words_to_marks(s):
    alphabet = string.ascii_lowercase
    return sum([alphabet.index(letter) + 1 for letter in s])
