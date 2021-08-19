T = int(input())
for _ in range(T):
    (n, m) = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    (i, j) = (0, 0)
    l = []
    while i < n and j < m:
        if a[i] < b[j]:
            l.append(a[i])
            i += 1
        elif a[i] == b[j]:
            i += 1
            j += 1
        else:
            l.append(b[j])
            j += 1
    while i < n:
        l.append(a[i])
        i += 1
    while j < m:
        l.append(b[j])
        j += 1
    print(*l)
