def ggt(a, b):
    while b != 0:
        c = a % b
        a, b = b, c
    return a


def kgv(a, b):
    return (a * b) / ggt(a, b)


case = int(input())

for l in range(case):
    n, k = list(map(int, input().split()))
    if n == 1:
        print("Yes")
    elif k == 0:
        print("No 1")
    else:
        cak = kgv(n, k) / k
        if cak == n:
            print("Yes")

        else:
            print("No %d" % cak)
