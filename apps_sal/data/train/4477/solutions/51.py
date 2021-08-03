def reverse_number(n):
    if abs(n) != n:
        num = str(n)[::-1]
        return int('-' + num[:-1])
    return int(str(n)[::-1])
