def rat_at(n):
    n = bin(n + 1)
    s = 1
    f = []
    if n[len(n) - 1] == '0':
        f.append(0)
    for i in range(len(n) - 1, 1, -1):
        if n[i] != n[i - 1]:
            f.append(s)
            s = 1
        else:
            s += 1
    num = [1, f[len(f) - 1]]
    for i in range(len(f) - 2, -1, -1):
        num[0] = f[i] * num[1] + num[0]
        (num[0], num[1]) = (num[1], num[0])
    (num[0], num[1]) = (num[1], num[0])
    return tuple(num)


def index_of(a, b):
    num = [b, a]
    f = []
    bin = ''
    l = '1'
    while num[0] != 0:
        (num[0], num[1]) = (num[1], num[0])
        f.append(num[0] // num[1])
        num[0] -= f[len(f) - 1] * num[1]
    if len(f) % 2 == 0:
        f[len(f) - 1] -= 1
        f.append(1)
    for n in f:
        bin = n * l + bin
        if l == '0':
            l = '1'
        else:
            l = '0'
    return int(bin, 2) - 1
