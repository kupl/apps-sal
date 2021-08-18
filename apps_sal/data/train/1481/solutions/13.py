t = int(input())
for _ in range(t):
    s = list(input())
    n = len(s)
    if(n % 2 == 1):
        print(-1)
    else:
        i = 0
        k1 = s.count('1')
        k2 = s.count('0')
        if(k1 == k2):
            print(0)
        elif(k1 == 0 or k2 == 0):
            print(-1)
        else:
            kmin = min(k1, k2)
            required = n // 2
            print(required - kmin)
