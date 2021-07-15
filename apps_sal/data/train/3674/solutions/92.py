def add_binary(a,b):
    i = a+b
    result = []
    while i >= 2:
        result.append(str(i % 2))
        i //= 2
    result.append(str(i % 2))
    return(''.join(result[::-1]))
