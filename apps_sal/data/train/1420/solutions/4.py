import math


def find_interleavings(a, b):
    c = list()

    def interleaf(i, j, l):
        if i == len(a) and j == len(b):
            c.append(tuple(l))
        elif i == len(a):
            interleaf(i, j + 1, l + [b[j]])
        elif j == len(b):
            interleaf(i + 1, j, l + [a[i]])
        else:
            interleaf(i + 1, j, l + [a[i]])
            interleaf(i, j + 1, l + [b[j]])
    interleaf(0, 0, [])
    return c


def find_interleavings_2(a, b, i, j):
    to_return = []
    if i == len(a) and j == len(b):
        return [[]]
    elif i == len(a):
        for leaf in find_interleavings_2(a, b, i, j + 1):
            to_return.append([b[j]] + leaf)
    elif j == len(b):
        for leaf in find_interleavings_2(a, b, i + 1, j):
            to_return.append([a[i]] + leaf)
    else:
        for leaf in find_interleavings_2(a, b, i, j + 1):
            to_return.append([b[j]] + leaf)
        for leaf in find_interleavings_2(a, b, i + 1, j):
            to_return.append([a[i]] + leaf)
    return to_return


for _ in range(int(input())):
    (n, m, k) = list(map(int, input().split(' ')))
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))
    res = 0
    ils = find_interleavings_2(a, b, 0, 0)
    ils = [tuple(x) for x in ils]
    memo = dict()
    for c in ils:
        try:
            res += memo[c]
            continue
        except KeyError:
            pass
        num_blocks = 0
        prev = math.inf
        for i in c:
            if i != prev:
                num_blocks += 1
            prev = i
        if num_blocks == k:
            res += 1
            memo[c] = 1
        else:
            memo[c] = 0
    print(res)
