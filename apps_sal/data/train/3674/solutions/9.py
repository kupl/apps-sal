def add_binary(a, b):
    n = a + b
    binList = []
    while n > 0:
        binList.append(n % 2)
        n = n // 2
    return ''.join(map(str, reversed(binList)))
