def single_digit(n):
    while n >= 10:
        n = sum((c == '1' for c in bin(n)))
    return n
