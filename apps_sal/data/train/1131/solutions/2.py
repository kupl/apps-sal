t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort()
    count = 1
    a = []
    for i in range(n - 1):
        if l[i] == l[i + 1]:
            count += 1
        else:
            if count > k:
                a.append(l[i])
                count = 1
    if count > k:
        a.append(l[-1])
    print(*a)
