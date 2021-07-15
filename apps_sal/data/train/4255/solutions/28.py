from string import ascii_lowercase, ascii_uppercase

def make_upper_case(s):
    return s.translate(str.maketrans(ascii_lowercase, ascii_uppercase))
