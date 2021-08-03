from string import ascii_lowercase, ascii_uppercase
trans = str.maketrans(ascii_lowercase, ascii_uppercase, ' ')


def vaporcode(s):
    return "  ".join(s.translate(trans))
