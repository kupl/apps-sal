n, a, q = int(input()), [*list(map(int, input().split()))], int(input())
ops = []

for i in range(q):
    t, *b = list(map(int, input().split()))
    ops.append((t, b))

b = [-1] * n
m = -1
for op, ar in reversed(ops):
    if op == 2:
        m = max(m, ar[0])
    else:
        p, x = ar
        p -= 1
        if b[p] == -1:
            b[p] = max(x, m)

print(' '.join(str(bi if bi != -1 else max(m, ai))for ai, bi in zip(a, b)))
