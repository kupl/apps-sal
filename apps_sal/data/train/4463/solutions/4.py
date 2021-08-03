import string


def alphabet_position(text):
    return " ".join([str(string.lowercase.index(letter.lower()) + 1) for letter in list(text) if letter.isalpha()])
