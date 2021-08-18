
for _ in range(int(input())):
    n = int(input())
    l = []
    for i in range(n):
        x, y = map(int, input().split())
        l.append((y, x))
    l.sort(reverse=True)

    y1, x1 = l[0]
    y2 = x2 = y3 = x3 = -1
    i = 1
    while i < n:
        y, x = l[i]
        if x == x1:
            p = 0
        else:
            y2, x2 = y, x
            break
        i += 1

    if i == n:
        print(0)
        continue
    while i < n:
        y, x = l[i]
        if x == x1 or x == x2:
            p = 1
        else:
            y3, x3 = y, x
            break
        i += 1
    if i == n:
        print(0)
        continue

    print(y3 + y2 + y1)
