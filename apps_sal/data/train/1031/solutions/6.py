from math import sqrt, pow
t = int(input())
while t > 0:
    (h, s) = list(map(int, input().split()))
    if pow(h, 2) + 4 * s >= 0 and pow(h, 2) - 4 * s >= 0:
        a = (sqrt(pow(h, 2) + 4 * s) + sqrt(pow(h, 2) - 4 * s)) / 2
        b = sqrt(pow(h, 2) + 4 * s) - a
        if a > 0 and b > 0:
            c = []
            c.append(a)
            c.append(b)
            c.append(h)
            c.sort()
            for i in c:
                print(i, end=' ')
            print(' ')
        else:
            print(-1, end=' ')
    else:
        print(-1)
    t -= 1
