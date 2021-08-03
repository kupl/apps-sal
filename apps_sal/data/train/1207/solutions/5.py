for _ in range(int(input())):
    n = int(input())
    ar = [int(x) for x in input().split()]
    if n == 1:
        print(ar[0])
    elif n == 2:
        print(ar[0] * ar[1])
    else:
        ar.sort()
        an = 0
        for i in range(1, n):
            an += ar[0] * ar[i]
        print(an)
