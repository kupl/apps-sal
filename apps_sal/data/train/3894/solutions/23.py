from string import ascii_lowercase


def solve(s):
    lowercase_counter = 0
    uppercase_counter = 0
    half_length = len(s) / 2
    for letter in s:
        if letter in ascii_lowercase:
            lowercase_counter += 1
            if lowercase_counter > half_length:
                return s.lower()
        else:
            uppercase_counter += 1
            if uppercase_counter > half_length:
                return s.upper()
    return s.lower()
