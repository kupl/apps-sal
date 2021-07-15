def find_digit(num, n):
    num = str(abs(num))
    return -1 if n < 1 else 0 if n > len(num) else int(num[-n])
