for _ in range(int(input())):
    n, c = map(int, input().split())
    pts_line, summation = {}, 0
    for _ in range(n):
        x, y = map(int, input().split())
        if((y - x, x % c) in pts_line):
            pts_line[(y - x, x % c)].append(x)
        else:
            pts_line[(y - x, x % c)] = [x]
    for pt in pts_line:
        arc = sorted(pts_line[pt])
        for metre in arc:
            summation += abs(metre - arc[len(arc) // 2]) // c
    print(len(pts_line), summation)
