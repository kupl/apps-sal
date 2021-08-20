for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = t = 0
    for i in range(n):
        if a[i] == 2:
            t += 1
            c += 1
        elif a[i] > 1:
            c += 1
    print(int(c * (c - 1) / 2 - t * (t - 1) / 2))
