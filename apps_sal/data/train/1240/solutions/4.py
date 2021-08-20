for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    for _ in range(n):
        if a[_] % 6 == 0:
            res += 6
        else:
            res += a[_] % 6
    print(res)
