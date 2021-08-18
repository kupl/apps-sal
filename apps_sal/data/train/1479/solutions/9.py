for _ in range(int(input())):
    n = int(input())
    d = {}
    for i in range(n):
        m, n = map(int, input().split())
        if m >= 1 and m <= 8:
            if m not in d:
                d[m] = n
            elif d[m] < n:
                d[m] = n
    print(sum(d.values()))
