def sum_digits(number):
    d = 0
    for c in str(abs(number)):
        d += ord(c) - 48
    return d
