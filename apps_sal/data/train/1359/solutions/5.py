for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    c = 0
    for i in l:
        if i % 2 == 0:
            c += 1
    if l[-1] % 2 == 1:
        a1 = c + (n - c - 1) * 2
        if c != 0:
            a2 = (n - c) + 2 * (c - 1)
        else:
            a2 = n
        if a1 > a2:
            print(a2)
        else:
            print(a1)
    else:
        a1 = (n - c) + (c - 1) * 2
        if c != n:
            a2 = c + (n - c - 1) * 2
        else:
            a2 = n
        if a1 > a2:
            print(a2)
        else:
            print(a1)
