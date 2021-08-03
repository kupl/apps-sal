import math
a = int(input())
while(a > 0):
    n, h = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort()
    x = l[-1]
    m = l[n // 2]
    for k in range(1, x + 1):
        y = math.ceil(m / k)
        if(y * n <= h):
            c = 0
            for i in l:
                c += math.ceil(i / k)
            if(c < h):
                k -= 1
                w = 0
                for i in l:
                    w += math.ceil(i / k)
                if(w <= h):
                    print(k)
                else:
                    print(k + 1)
                break
            elif(c == h):
                w = 0
                for i in l:
                    w += math.ceil(i / k)
                if(w == h):
                    print(k)
                elif(w > h):
                    print(k + 1)
                break
    a -= 1
