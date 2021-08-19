t = int(input())
while t > 0:
    n = int(input())
    l = list(map(int, input().split()))
    x = l[1] - l[0]
    if l[2] - l[1] == l[3] - l[2] and l[2] - l[1] != x:
        l[0] = -l[2] + 2 * l[1]
    elif l[2] - l[1] != x and l[3] - l[2] != l[2] - l[1] and (l[3] - l[2] != x):
        y = l[3] - l[0]
        y //= 3
        if x == y:
            l[2] = l[1] + x
        else:
            l[1] = l[0] + y
    else:
        for i in range(2, n):
            if l[i] != l[i - 1] + x:
                l[i] = l[i - 1] + x
                break
    print(*l)
    t -= 1
