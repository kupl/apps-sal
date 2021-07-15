def single_digit(n):
    if n < 10:
        return n
    return single_digit(bin(n).count('1'))
