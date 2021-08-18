from collections import Counter
for z in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for j in range(n):
        b.append((a[j], j))
    c = Counter(a)
    m = 0
    for x, y in c.items():
        m = max(y, m)
    if m > n - m:
        print("No")
    else:
        d = [0] * n
        b.sort()
        for i in range(n):
            d[b[i][1]] = b[i - m][0]
        print("Yes")
        for i in d:
            print(i, end=" ")
        print()
