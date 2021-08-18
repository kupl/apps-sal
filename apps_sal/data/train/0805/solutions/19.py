t = int(input())
while(t > 0):
    t -= 1
    v1 = []
    v1.clear()
    n = int(input())
    a = 0
    b = 0
    while(n > 0):
        n -= 1
        s, p, v = map(int, input().split())

        if(p % (s + 1) == 0):
            a = p // (s + 1)
            a = a * v
            v1.append(a)
        else:
            b = p // (s + 1)
            b = b * v
            v1.append(b)
    print(max(v1))
