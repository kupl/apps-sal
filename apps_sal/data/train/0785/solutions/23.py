t = int(input())
while(t > 0):
    n = int(input())
    g = 0
    i = 0
    x = 0
    d = 0
    h = 0
    p = 1
    mp = 0
    while(p > 0):
        x = 1 << i
        g = g + x
        i += 1
        h = h + n
        p = h - g
        if(mp < p):
            d = i
            mp = p
        if(i > 50):
            break
    print(i - 1, d)
    t -= 1
