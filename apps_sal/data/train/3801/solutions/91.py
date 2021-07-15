import string

def words_to_marks(s):
    alphabet = ' ' + string.ascii_lowercase
    return sum([alphabet.index(letter) for letter in s])
