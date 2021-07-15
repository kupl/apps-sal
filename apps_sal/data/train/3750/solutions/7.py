def count_letters_and_digits(s):
    return bool(s) and sum(map(str.isalnum, s))
