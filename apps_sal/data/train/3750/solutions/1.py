def count_letters_and_digits(s):
    return sum(map(str.isalnum, s))
