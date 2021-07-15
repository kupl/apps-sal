def single_digit(n):
    while n > 9:
        n = sum(1 if i == "1" else 0 for i in bin(n))
    return n
