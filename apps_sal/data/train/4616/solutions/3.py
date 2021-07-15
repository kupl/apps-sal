def single_digit(n):
    if len(str(n)) == 1:
        return n
    else:
        return single_digit(bin(n)[2:].count('1'))
