def climb(n):
    arr = []
    while n:
        arr.append(n)
        n //= 2
    return arr[::-1]
