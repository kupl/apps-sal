def reverse_number(n):
    if n < 0:
        s = str(n)[1:]
        return int(s[::-1]) * -1
    return int(str(n)[::-1])
