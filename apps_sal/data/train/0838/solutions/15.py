for _ in range(int(input())):
    n = int(input())
    ar = [int(x) for x in input().split()]
    an = max(ar)
    d = 1
    for i in range(1, n):
        if an - d < ar[i]:
            an += ar[i] - (an - d)
        d += 1
    print(an)
