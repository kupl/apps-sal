for x in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    c = 1
    t = l[0]
    for y in range(1, n):
        if l[y] <= t:
            c += 1
            t = l[y]
    print(c)
