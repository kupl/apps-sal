from math import gcd
for t in range(int(input())):
    n = int(input())
    a = sorted(set(int(i) for i in input().split()))
    l = len(a)
    for j in range(l - 1):
        if gcd(a[j], a[j + 1]) == 1:
            print(n)
            break
    else:
        print(-1)
