for u in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    m = 10 ** 10
    for i in range(1, n):
        x = l[i] - l[i - 1]
        m = min(m, x)
    print(m)
