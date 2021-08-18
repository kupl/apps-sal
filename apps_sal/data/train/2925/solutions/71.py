def multiply(n):
    num = len(str(n))
    if n < 0:
        num -= 1
    return n * 5 ** num
