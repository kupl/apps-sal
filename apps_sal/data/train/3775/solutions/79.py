def digits(n):
    num = 0
    while n > 0:
        n = int(n / 10)
        num = num + 1
    return num
