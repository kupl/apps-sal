for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mx = 1
    if n > 1 and a[0] == a[1]:
        mx = 2
    if n > 2:
        c = 1
        f = 1
        for i in range(2, n):
            if a[i] == a[i - 1] + a[i - 2]:
                c += 1 + f
                f = 0
                continue
            else:
                mx = max(c, mx)
                c = 1
                f = 1
        mx = max(c, mx)
    print(mx)
