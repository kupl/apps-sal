for i in range(int(input())):
    a, b = map(int, input().split())
    b = bin(b)[2:]
    b = list(map(str, b))
    for j in range(len(str(bin(a)[2:])) - len(b)):
        b.insert(0, "0")
    xor = a ^ int(("".join(b)), 2)
    max = xor
    c = 0
    for j in range(len(b) - 1):
        b = (b[-1:] + b[:-1])
        xor = a ^ int(("".join(b)), 2)
        if xor > max:
            max = xor
            c = j + 1
    print(c, max)
