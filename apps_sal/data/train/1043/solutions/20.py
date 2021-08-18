for _ in range(int(input())):
    n, k = map(int, input().split())
    ns = [i for i in input().split()]
    d = {}
    for i in ns:
        d[i] = False
    for i in range(k):
        ks = list(map(str, input().split()))
        for j in ks:
            if j in d:
                d[j] = True
    for i in ns:
        if d[i] == True:
            print("YES", end=' ')
        else:
            print("NO", end=' ')

    print()
