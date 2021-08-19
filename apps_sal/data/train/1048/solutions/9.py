for _ in range(int(input())):
    (a, k) = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort()
    p = l[0] + a / 2 + k
    q = l[2] - a / 2 - k
    print(format(0 if p < q else a * min(a, p - q), 'f'))
