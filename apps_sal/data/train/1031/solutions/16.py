from math import sqrt
for p in range(int(input())):
    h, s = list(map(int, input().split()))
    x = h**4 - 16 * (s**2)
    if x < 0:
        print(-1)
    else:
        a = (h**2 + sqrt(x)) / 2
        if(a < 0):
            print(-1)
        else:
            len2 = sqrt(h**2 - a)
            len1 = sqrt(a)
            if len1 > len2:
                print(len2, len1, h)
            else:
                print(len1, len2, h)
