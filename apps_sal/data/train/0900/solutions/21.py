import math
t = int(input())
while(t > 0):
    k = int(input())
    j = 0
    h = math.pow(10, k) - 1
    h = int(h)
    c = 0
    for i in range(h + 1):
        ab = []
        if(i == 0):
            if(i not in ab):
                ab.append(i)
            p = h - i
            while(p > 0):
                g = p % 10
                if(g not in ab):
                    ab.append(g)
                p = p // 10
        elif(i == h):
            if(i not in ab):
                ab.append(h - i)
            p = i
            while(p > 0):
                g = p % 10
                if(g not in ab):
                    ab.append(g)
                p = p // 10

        else:
            p = i
            while(p > 0):
                g = p % 10
                if (g not in ab):
                    ab.append(g)
                p = p // 10
            p = h - i
            while(p > 0):
                g = p % 10
                if(g not in ab):
                    ab.append(g)
                p = p // 10
        if(len(ab) == 2):
            c += 1
    print(c)
    t -= 1
