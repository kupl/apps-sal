import string


def reverse_letter(input_str):
    return ''.join([c for c in input_str if c in string.ascii_letters][::-1])
