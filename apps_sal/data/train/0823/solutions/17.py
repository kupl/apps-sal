# cook your dish here
for _ in range(int(input())):
    a = list(map(int, input().split()))
    test = 0
    n = 4
    for mask in range(1, 1 << n):
        s = 0

        for i in range(n):
            if mask & 1 << i:
                s += a[i]
        if s == 0:
            test = 1
            print('Yes')
            break
    if not test:
        print('No')
