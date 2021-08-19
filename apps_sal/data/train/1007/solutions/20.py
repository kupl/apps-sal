from math import gcd


def largestgcd():
    n = int(input())
    ls = list(map(int, input().split()))
    gc = 0
    f = 0
    for i in range(n):
        gc = gcd(gc, ls[i])
        if gc == 1:
            f = 1
            break
    if f == 1:
        print(n)
    else:
        print(-1)


def __starting_point():
    for _ in range(int(input())):
        largestgcd()


__starting_point()
