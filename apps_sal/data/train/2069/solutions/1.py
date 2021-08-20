n = int(input())
a = list(map(int, input().split()))
if n != 1:
    print(n, n)
    print(-a[-1])
    print(1, n - 1)
    res_2 = [a[i] * (n - 1) for i in range(n - 1)]
    print(*res_2)
    print(1, n)
    res_3 = [-a[i] * n for i in range(n)]
    res_3[-1] = 0
    print(*res_3)
else:
    print(1, 1)
    print(-a[0])
    print(1, 1)
    print(0)
    print(1, 1)
    print(0)
