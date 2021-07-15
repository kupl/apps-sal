def count_letters_and_digits(s):
    return isinstance(s, str) and sum(map(str.isalnum, s))
