t = int(input())
while t > 0:
    s = 0
    (a, b) = input().split()
    a = int(a)
    for i in range(a):
        l = input()
        if 'CONTEST_WON' in l:
            (c, d) = l.split()
            d = int(d)
            if d < 20:
                s += 320 - d
            else:
                s += 300
        elif 'TOP_CONTRIBUTOR' in l:
            s += 300
        elif 'BUG_FOUND' in l:
            (e, f) = l.split()
            f = int(f)
            s += f
        else:
            s += 50
    if b == 'INDIAN':
        print(s // 200)
    else:
        print(s // 400)
    t -= 1
