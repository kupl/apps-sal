for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))[:n]
    l.sort()
    a = l[0] - k
    b = l[-1] + k
    print(b - a)
