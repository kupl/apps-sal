def string_clean(s):
    return s.translate(s.maketrans(' ', ' ', '1234567890'))
