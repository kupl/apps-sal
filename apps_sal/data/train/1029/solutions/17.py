t = int(input())
for i in range(t):
    b = []
    (n, m) = input().split()
    (n, m) = (int(n), int(m))
    a = input().split()
    for j in range(m):
        a[j] = int(a[j])
    p = 1
    while p <= n:
        if p not in a:
            b.append(p)
            p = p + 1
        else:
            p = p + 1
    for j in range(0, len(b), 2):
        print(b[j], end=' ')
    print()
    for j in range(1, len(b), 2):
        print(b[j], end=' ')
    print()
