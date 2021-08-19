# cook your dish here
import math
test = int(input())
while(test > 0):
    a, b, c, d = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)

    if d == c:
        if a == b:
            print("YES")
        else:
            print("NO")
    else:
        m = abs((a - b) / (c - d))
        if int(m) == m:
            if min(a, b) + (max(c, d) * m - 1) == max(a, b) + (min(c, d) * m - 1):
                print("YES")
            else:
                print("NO")

        else:
            m = math.ceil(m)
            if min(a, b) + (max(c, d) * m) == max(a, b) + (min(c, d) * m):
                print("YES")
            else:
                print("NO")
    test = test - 1
