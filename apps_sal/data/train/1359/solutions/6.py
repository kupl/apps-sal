for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    even = 0
    for a in l:
        if a % 2 == 0:
            even += 1
    if l[-1] % 2 == 0:
        a = (n - even) + (even - 1) * 2
        if even != n:
            b = even + (n - even - 1) * 2
        else:
            b = n
        if a > b:
            print(b)
        else:
            print(a)
    else:
        a = even + (n - even - 1) * 2
        if even != 0:
            b = (n - even) + 2 * (even - 1)
        else:
            b = n
        if a > b:
            print(b)
        else:
            print(a)
