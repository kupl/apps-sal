def reverse_number(n):
    return int((n < 0 and '-' or '') + str(abs(n))[::-1])


