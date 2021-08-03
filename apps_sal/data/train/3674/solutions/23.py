def add_binary(a, b):
    return toBinary(a + b)


def toBinary(n):
    result = ''
    while n > 1:
        result += str(n % 2)
        n = n // 2
    result += str(n % 2)
    return result[::-1]
