def multiply(n):
    return n * 5 ** int_len(n)


def int_len(n):
    n = abs(n)
    length = 0
    while n:
        length += 1
        n //= 10
    return length
