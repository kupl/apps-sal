n, m, c = list(map(int, input().split()))
bit = [0] * (n + 1)


def add(index, val):
    index += 1
    while index <= n:
        bit[index] += val
        index += index & -index


def get(index):
    r = 0
    index += 1
    while index:
        r += bit[index]
        index -= index & -index
    return r


while m:
    m -= 1
    op = input().split()
    if len(op) == 4:
        _, u, v, k = op
        u = int(u)
        v = int(v)
        k = int(k)
        u -= 1
        v -= 1
        add(u, k)
        add(v + 1, -k)
    else:
        _, p = op
        p = int(p)
        print(get(p - 1) + c)
