for u in range(int(input())):
    n, k = list(map(int, input().split()))
    l = list(map(int, input().split()))
    c = 1
    m = 0
    for i in range(n - 1):
        if(l[i] == l[i + 1]):
            c += 1
            m = max(m, c)
        else:
            c = 1
    m = max(m, c)
    print(m)
