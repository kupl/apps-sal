def add_binary(a, b):
    binaryNum = ""
    q = 0
    mod = 0
    cSum = a + b
    while cSum > 0:
        mod = cSum % 2
        cSum //= 2
        binaryNum += str(mod)
    return binaryNum[::-1]
