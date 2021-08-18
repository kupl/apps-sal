t = int(input())
while(t != 0):
    x, y = map(int, input().split())
    s = 0
    i = 1
    while(i != -1):
        q = y * i
        if q < 10:
            s += q
        else:
            s += (q % 10)
        i += 1
        if i * y > x:
            i = -1

    print(s)
    t -= 1
