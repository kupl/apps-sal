from math import gcd
for _ in range(int(input())):

    n = int(input())
    l = list(map(int, input().split()))

    g = l[0]

    for x in l:
        g = gcd(x, g)

    if g == 1:
        print(-1)
    elif g % 2 == 0:
        print(2)
    else:

        for i in range(3, int((g)**0.5) + 1):

            if g % i == 0:

                print(i)
                break
        else:
            print(g)
