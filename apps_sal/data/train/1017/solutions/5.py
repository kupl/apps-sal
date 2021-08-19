for _ in range(int(input())):
    a = list(map(int, input().split()))
    p = a[-1]
    a = a[:-1]
    for i in range(len(a)):
        a[i] = a[i] * p
    b = sum(a)
    if b > 24 * 5:
        print('Yes')
    else:
        print('No')
