def is_digit(n):
    return sum([x in '0123456789' for x in str(n)]) == len(n) and len(str(n)) == 1
