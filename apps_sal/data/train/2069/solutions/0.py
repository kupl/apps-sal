n = int(input())
L = list(map(int, input().split()))
if n == 1:
    print(1, 1)
    print(0)
    print(1, 1)
    print(0)
    print(1, 1)
    print(-L[0])
else:
    print(1, n - 1)
    for i in range(n - 1):
        print(L[i] * (n - 1), end=' ')
    print()
    print(n, n)
    print(-L[n - 1])
    print(1, n)
    for i in range(n - 1):
        print(-L[i] * n, end=' ')
    print(0)
