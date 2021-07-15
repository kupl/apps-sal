def reverse_number(n):
    return (1 - 2 * (n < 0)) * int(str(abs(n))[::-1])
