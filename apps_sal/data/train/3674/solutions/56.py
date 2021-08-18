def add_binary(a, b):
    c = a + b

    x = 0
    while 2**x <= c:
        x += 1

    if 2**x > c:
        x -= 1

    reverse = [i for i in range(x + 1)]
    reverse = reverse[::-1]
    print(reverse)

    res = ""
    for i in reverse:
        if 2**i <= c:
            c -= 2**i
            res += "1"
        else:
            res += "0"

    return res
