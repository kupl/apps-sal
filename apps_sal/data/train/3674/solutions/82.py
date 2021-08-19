def add_binary(a, b):
    # return bin(a+b)[2:]
    if a == 0 and b == 0:
        return ''
    elif a & b & 1:
        return add_binary(a // 2 + 1, b // 2) + '0'
    elif (a | b) & 1:
        return add_binary(a // 2, b // 2) + '1'
    else:
        return add_binary(a // 2, b // 2) + '0'
