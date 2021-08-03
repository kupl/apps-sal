import math
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    for i in range(1, n):
        l[i] = math.gcd(l[i], l[i - 1])
    a = l[-1]
    if a == 1:
        print(-1)
    else:
        f = 0
        p = int(math.sqrt(l[-1]))
        i = 2
        while i <= p:
            if a % i == 0:
                print(i)
                f = 1
                break
            i += 1
        if f == 0:
            print(a)
