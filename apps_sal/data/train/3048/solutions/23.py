from string import ascii_lowercase, ascii_uppercase
translation_table = str.maketrans(ascii_lowercase + ascii_uppercase, ascii_uppercase + ascii_lowercase)


def alternateCase(s):
    return s.translate(translation_table)
