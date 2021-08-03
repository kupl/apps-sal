for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mx = 1
    if n < 3:
        if n == 2 and a[0] == a[1]:
            mx = 2
    else:
        c = 2
        for i in range(2, n):
            if a[i] == a[i - 1] + a[i - 2]:
                c += 1
                continue
            else:
                mx = max(c, mx)
                c = 2
        mx = max(c, mx)
    print(mx)
