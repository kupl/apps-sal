def reverse_number(n):
    return int(str(abs(n))[::-1]) *n//max(abs(n),1)
