import math
for i in range(int(input())):
    (h, a) = list(map(int, input().split()))
    cv = 4 * a / h ** 2
    if cv > 1:
        print(-1)
    else:
        thita = math.asin(cv) / 2
        ratio = math.tan(thita)
        hh = math.sqrt(2 * a / ratio)
        b = 2 * a / hh
        m = max(b, hh)
        s = min(b, hh)
        print('%0.5f %0.5f %0.5f' % (s, m, h))
