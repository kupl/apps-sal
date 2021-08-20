for _ in range(int(input())):
    (n, k, x) = map(int, input().split())
    a = []
    if k % 2 == 0:
        for i in range(1, k):
            a.append(0)
        a.append(x)
    else:
        for i in range(1, k):
            a.append(0)
        a.append(x)
    b = []
    j = 0
    for i in range(n):
        if j == len(a):
            j = 0
        b.append(a[j])
        j = j + 1
    for i in b:
        print(i, '', end='')
    print()
