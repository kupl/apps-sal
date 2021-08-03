t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))[:n]
    l = []
    for j in range(len(a)):
        for k in range(j + 1, len(a)):
            l.append(a[j] + a[k])
    print(l.count(max(l)) / ((n * (n - 1)) / 2))
