for _ in range(int(input())):
    n = int(input())
    ar = [int(x) for x in input().split()]
    ar.sort(reverse=True)
    s = 0
    for i in range(0, n, 2):
        s += ar[i]
    print(s)
