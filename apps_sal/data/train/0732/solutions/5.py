for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    an = 0
    pa, pb = 0, 0
    for i in range(n):
        if a[i] == b[i] and pa == pb:
            an += a[i]
        pa += a[i]
        pb += b[i]
    print(an)
