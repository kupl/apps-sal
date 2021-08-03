t = int(input())

for _ in range(t):
    n, k = [int(x) for x in input().split()]

    a = []
    for i in range(1, n + 1):
        a.append(str(i))

    ans = a[n - k - 1:] + a[:n - k - 1]

    print(" ".join(ans))
