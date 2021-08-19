t = int(input())
for i in range(t):
    (n, m) = map(int, input().split())
    a = [0] * 11
    for j in range(1, 11):
        a[j] = m * j % 10 + a[j - 1]
    x = n // m
    print(a[10] * (x // 10) + a[x % 10])
