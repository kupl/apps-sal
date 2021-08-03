# cook your dish here
for _ in range(int(input())):
    a = list(map(int, input().split()))
    n = 4
    test = 0
    for mask in range(1, 1 << n):
        s = set()
        for i in range(n):
            f = 1 << i
            if mask & f != 0:
                s.add(a[i])
        if sum(s) == 0:
            test = 1
            break
    if test:
        print('Yes')
    else:
        print('No')
