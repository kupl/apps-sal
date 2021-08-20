def reverse_number(n):
    return int(str(n)[::-1] if n >= 0 else '-' + str(n)[::-1][0:-1])
