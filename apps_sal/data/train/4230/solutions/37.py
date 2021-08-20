import string


def reverse_letter(str):
    chars = string.ascii_lowercase
    return ''.join((i for i in str[::-1] if i in chars))
