for _ in range(int(input())):
    n, k, x = map(int, input().split())
    a = []
    if(k == 1):
        for i in range(n):
            print(x, end=' ')
    else:
        a.append(x)
        for i in range(k - 1):
            a.append(0)
        j = 0
        p = 0
        for i in range(n):
            if(i < len(a) - 1):
                print(a[i], end=' ')
            else:
                j = i % len(a)
                print(a[j], end=' ')
    print()
