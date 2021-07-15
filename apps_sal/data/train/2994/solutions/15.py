def find_digit(num, n):
    if n <= 0:
        return -1
    return abs(num) % 10**n // 10**(n-1)
