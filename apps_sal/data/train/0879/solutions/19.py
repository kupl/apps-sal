for _ in range(int(input())):
    x, y = map(int, input().split())
    l = []
    s = 0
    y1 = y
    i = 1
    while(y1 * i <= x):
        l.append(str(y1 * i))
        i += 1
    for i in l:
        s += int(i[-1])
    print(s)
