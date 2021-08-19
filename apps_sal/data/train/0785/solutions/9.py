for _ in range(int(input())):
    a = int(input())
    D1 = 0
    D2 = [1, 1 - a]
    pd1 = a
    i = 1
    pd2 = 2 ** (i - 1)
    while pd1 + a > pd2 + 2 ** i:
        i += 1
        pd1 += a
        pd2 = pd2 + 2 ** (i - 1)
        if D2[1] < pd1 - pd2:
            D2[1] = pd1 - pd2
            D2[0] = i
    print(i, D2[0])
