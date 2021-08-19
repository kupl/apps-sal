for _ in range(int(input())):
    a = (int(i) for i in input().split())
    a = sorted(a)
    if a[2] <= a[0] + a[1] + 1:
        print('Yes')
    else:
        print('No')
