import string


def unused_digits(*args):
    found_digits_chars = {char for n in args for char in str(n)}

    all_digits_chars = set(string.digits)
    unused_digits_chars = all_digits_chars - found_digits_chars

    return ''.join(sorted(list(unused_digits_chars)))
