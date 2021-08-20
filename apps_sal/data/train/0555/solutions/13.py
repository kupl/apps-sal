for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = 2
    m = 0
    for i in range(2, n):
        if a[i] == a[i - 1] + a[i - 2]:
            c += 1
        else:
            m = max(c, m)
            c = 2
    m = max(c, m)
    print(m)
