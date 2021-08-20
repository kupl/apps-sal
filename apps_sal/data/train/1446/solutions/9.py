t = int(input())
while t > 0:
    n = int(input())
    if n == 1:
        print(2)
    else:
        q = 0
        for i in range(1, 31):
            p = 1 << i
            if p ^ p - 1 == n:
                print(p - 1)
                q = 1
                break
        if q == 0:
            print(-1)
    t -= 1
