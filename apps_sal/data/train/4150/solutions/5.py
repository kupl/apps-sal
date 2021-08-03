from string import ascii_letters, ascii_lowercase, ascii_uppercase


def shift(s, n):
    return s[n:] + s[:n]


table = str.maketrans(
    ascii_letters,
    shift(ascii_lowercase, 13) + shift(ascii_uppercase, 13))


def rot13(message):
    return message.translate(table)
