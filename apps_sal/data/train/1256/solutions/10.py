for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    t = 0
    m = 0
    for i in range(n):
        if a[i] == 2:
            t += 1
        if a[i] > 2:
            m += 1
    print(t * m + m * (m - 1) // 2)
