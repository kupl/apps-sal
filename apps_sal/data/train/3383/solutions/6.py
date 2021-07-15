def is_even(n):
    return str(bin(n)[2:])[-1] == '0'
