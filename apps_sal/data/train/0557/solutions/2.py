t = int(input())
for _ in range(t):
    (n, m) = map(int, input().split())
    a = list()
    for _ in range(n):
        a.append(10)
    for _ in range(m):
        (i, j, k) = map(int, input().split())
        for z in range(i - 1, j):
            a[z] = a[z] * k
print(sum(a) // n)
