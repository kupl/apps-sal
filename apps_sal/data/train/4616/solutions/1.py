def single_digit(n):
    while n > 9:
        n = int(bin(n).count('1'))
    return n
