def add_binary(a, b):
    # your code here
    res = ''
    c = a + b

    while c > 1:
        rem = c % 2
        res += str(rem)
        c = c // 2

    res += str(1)
    return (''.join(list(reversed(res))))
