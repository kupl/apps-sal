import math
from decimal import *
T = int(input())
while T > 0:
    h, a = list(map(int, input().split()))
    x = h * h * h * h - 16 * a * a
    if x < 0:
        print(-1)
    else:
        y = 0.5 * h * h - 0.5 * math.sqrt(x)
        if y < 0:
            print(-1)
        else:
            s = math.sqrt(0.5 * h * h - 0.5 * math.sqrt(x))
            b = h * h - s * s
            ans = []
            ans.append(s)
            ans.append(math.sqrt(b))
            ans.append(h)
            new_list = []
            for item in ans:
                new_list.append(float(item))
            ans.sort()
            print(format(ans[0], '.6f'), format(ans[1], '.6f'), format(ans[2], '.6f'))
            # print ans[0],ans[1],ans[2]
    T -= 1
