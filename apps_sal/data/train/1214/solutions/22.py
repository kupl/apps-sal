t = int(input())
q = 0
while(t):
    q += 1
    t -= 1
    m, n = input().split()
    m = int(m)
    n = int(n)
    rx, ry = input().split()
    rx = int(rx)
    ry = int(ry)
    l = int(input())
    a = input().split()
    a = str(a)
    x = y = 0
    for i in range(2, l + 2):
        if a[i] == 'L':
            x -= 1
        elif a[i] == 'R':
            x += 1
        if a[i] == 'U':
            y += 1
        elif a[i] == 'D':
            y -= 1
    if x == rx and y == ry:
        print("Case " + str(q) + ": REACHED")
    elif (x > m or x < 0) or (y < 0 or y > n):
        print("Case " + str(q) + ": DANGER")
    else:
        print("Case " + str(q) + ": SOMEWHERE")
