from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def solve(s):
    return [len([q for q in s if q in ascii_uppercase]), len([q for q in s if q in ascii_lowercase]), len([q for q in s if q in digits]), len([q for q in s if q in punctuation])]
