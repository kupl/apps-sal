from string import ascii_lowercase


def to_lover_case(s):
    return s.lower().translate(str.maketrans(ascii_lowercase, ('LOVE' * 7)[:26]))
