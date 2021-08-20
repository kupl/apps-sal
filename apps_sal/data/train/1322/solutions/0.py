for i in range(int(input())):
    (n, k) = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    c = 0
    for i in l:
        if i >= l[k - 1]:
            c += 1
    print(c)
