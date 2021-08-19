for _ in range(int(input())):
    (a, b) = list(map(int, input().split()))
    s = max(max(a, b), 2 * min(a, b))
    print(s * s)
