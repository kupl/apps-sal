t = int(input())
while t:
    (n, k, l) = map(int, input().split())
    if k * l < n:
        print(-1)
    elif k == 1 and n > 1:
        print(-1)
    else:
        (a, b) = divmod(n, k)
        l = [i for i in range(1, k + 1)]
        print(*a * l + l[:b])
    t -= 1
