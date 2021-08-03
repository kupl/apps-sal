t = int(input())
for _ in range(t):
    n = int(input())
    k = int(input())
    x1 = k // n
    y1 = (x1 + 1)
    y2 = k % n
    x2 = n - y2
    ans = 0
    i = 0
    j = 0
    l = []
    while i < x2 and j < y2:
        if y2 >= x2:
            l += [1, 0]
        else:
            l += [0, 1]
        i += 1
        j += 1
    while i < x2:
        l.append(0)
        i += 1
    while j < y2:
        l.append(1)
        j += 1
    ans = 0
    for i in range(1, len(l)):
        ans += abs(l[i] - l[i - 1])
    print(ans)
