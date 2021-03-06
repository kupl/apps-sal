for cas in range(eval(input())):
    n = eval(input())
    pts = []
    for i in range(n):
        (x, y) = list(map(int, input().strip().split()))
        pts.append((x, y))
    minx = min((x for (x, y) in pts))
    maxx = max((x for (x, y) in pts))
    miny = min((y for (x, y) in pts))
    maxy = max((y for (x, y) in pts))
    for i in range(n):
        if pts[i] == (minx, miny):
            print('1\n%d NE' % (i + 1))
            break
        if pts[i] == (minx, maxy):
            print('1\n%d SE' % (i + 1))
            break
        if pts[i] == (maxx, miny):
            print('1\n%d NW' % (i + 1))
            break
        if pts[i] == (maxx, maxy):
            print('1\n%d SW' % (i + 1))
            break
    else:
        mini = min(list(range(n)), key=lambda i: pts[i])
        maxi = max(list(range(n)), key=lambda i: pts[i])
        if pts[mini][1] < pts[maxi][1]:
            print('2\n%d NE\n%d SW' % (mini + 1, maxi + 1))
        else:
            print('2\n%d SE\n%d NW' % (mini + 1, maxi + 1))
