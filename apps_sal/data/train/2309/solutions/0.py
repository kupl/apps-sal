d = [-1] * 1000001
for t in range(int(input())):
    n, a = int(input()), list(map(int, input().split()))
    a.sort()
    for i in range(n):
        for j in range(i + 1, n):  d[a[j] - a[i]] = t
    i = 1
    while any(d[i * j] == t for j in range(1, n)): i += 1
    print("YES\n" + ' '.join(str(j * i + 1) for j in range(n)))
