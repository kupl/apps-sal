for i in range(int(input())):
    import math
    n = int(input())
    f = c = 0
    while(n >= 1):
        f = math.floor(math.sqrt(n))
        c += 1
        n = n - f * f
    print(c)
