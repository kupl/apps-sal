def reverse_number(n):
    if n < 0:
        return int('-' + str(abs(n))[::-1])
    return int(str(n)[::-1])
