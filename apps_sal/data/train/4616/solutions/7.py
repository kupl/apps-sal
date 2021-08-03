def single_digit(n):
    while n / 10 >= 1:
        n = sum(map(int, bin(n)[2:]))
    return n
