def find_digit(num, n):
    if n <= 0:
        return -1
    num = str(abs(num))
    return len(num) >= n and int(num[-n])
