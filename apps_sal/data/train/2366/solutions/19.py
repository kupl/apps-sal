def int_multiple():
    return [int(c) for c in input().split()]


def int_single():
    return int(input())


def str_multiple():
    return [c for c in input().split()]


def str_single():
    return input()


t = int_single()

res = []

for i in range(t):
    n = int_single()
    l = int_multiple()
    cnt = 0
    mn = l[-1]
    for j in reversed(list(range(n))):
        if l[j] < mn:
            mn = l[j]
        if l[j] > mn:
            cnt += 1

    res.append(cnt)

for r in res:
    print(r)
