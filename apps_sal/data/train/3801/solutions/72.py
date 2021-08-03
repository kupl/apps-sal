import string


def words_to_marks(word):
    alphabet = {char: i for i, char in enumerate(string.ascii_lowercase, start=1)}

    values = [alphabet[letter] for letter in word if letter in alphabet]
    return sum(values)
