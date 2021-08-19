from math import copysign


def main():
    a = [int(c) for c in input().split()]
    assert 0 not in a
    k = len(a)
    prv = []
    cur = []
    for (i, e) in enumerate(a):
        if i % 2:
            cur.append(a[i])
        else:
            prv.append(a[i])
    n = len(prv)
    if len(cur) < n:
        cur.append(0)
    if copysign(1, prv[0]) != copysign(1, cur[0]):
        return 0
    for r in range(k - 2):
        nxt = [cur[0] * prv[i] - prv[0] * cur[i] for i in range(1, n)] + [0]
        if nxt == [0] * n:
            for i in range(n):
                nxt[i] = cur[i] * (k - r - 2 * i)
        (prv, cur) = (cur, nxt)
        if copysign(1, prv[0]) != copysign(1, cur[0]) or cur[0] == 0:
            return 0
    return 1


for _ in range(int(input())):
    print(main())
