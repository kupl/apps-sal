a = int(input())
for i in range(a):
    d = []
    b = int(input())
    for j in range(b):
        d.append(list(map(int,input().split())))
    mix = -100000
    miy = mix
    maxx = 100000
    maxy = maxx
    f = True
    for j in range(b):
        x = d[j][0]
        y = d[j][1]
        if d[j][2] == 0:
            if x > maxx:
                print(0)
                f = False
                break
            mix = max(mix, x)
        if d[j][3] == 0:
            if y < miy:
                print(0)
                f = False
                break
            maxy = min(maxy, y)
        if d[j][5] == 0:
            if y > maxy:
                print(0)
                f = False
                break
            miy = max(miy, y)
        if d[j][4] == 0:
            if x < mix:
                print(0)
                f = False
                break
            maxx = min(maxx, x)
    if f:
        print(1, mix, miy)

