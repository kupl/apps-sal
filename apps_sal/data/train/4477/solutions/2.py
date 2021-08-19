def reverse_number(n):
    if str(n)[0] == '-':
        return -int(str(n)[:0:-1])
    else:
        return int(str(n)[::-1])
