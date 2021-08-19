from string import ascii_letters
t = str.maketrans(ascii_letters, ('LOVE' * 7)[:26] * 2)


def to_lover_case(string):
    return string.translate(t)
