# cook your dish here
for _ in range(int(input())):
    a = [int(x) for x in input().split()]
    n = 4
    tot = 1 << n
    flag = False
    for mask in range(tot):
        s = []
        for i in range(n):
            f = 1 << i
            if mask & f != 0:
                s.append(a[i])
        if len(s) != 0 and sum(s) == 0:
            flag = True
            break
    if flag:
        print('Yes')
    else:
        print('No')
