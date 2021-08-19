import math
t = int(input())
while t > 0:
    (h, s) = list(map(int, input().split()))
    check = h * h - 4 * s
    if h * h >= 4 * s:
        det = math.sqrt(h * h * h * h - 16 * s * s)
        a = (h * h + det) / 2
        a = math.sqrt(a)
        b = (h * h - det) / 2
        b = math.sqrt(b)
        if a < b:
            print('%f %f %f' % (a, b, h))
        else:
            print('%f %f %f' % (b, a, h))
    else:
        print('-1')
    t -= 1
