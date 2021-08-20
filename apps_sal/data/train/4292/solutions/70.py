def string_clean(s):
    return ''.join((letter for letter in s if not letter.isnumeric()))
