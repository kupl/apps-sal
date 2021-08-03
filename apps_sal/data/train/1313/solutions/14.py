import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    g = a[0]
    for i in a:
        g = math.gcd(g, i)
    if g == 1:
        print(-1)
    else:
        for i in range(2, int(math.sqrt(g)) + 1):
            if g % i == 0:
                print(i)
                break
        else:
            print(g)
