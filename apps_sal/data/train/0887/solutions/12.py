t = int(input())
for _ in range(t):
    n = int(input())
    a1 = input()
    b1 = input()
    a = list(map(int, a1.split()))
    b = list(map(int, b1.split()))
    c1 = a.count(0)
    c2 = b.count(0)
    flag = False
    if c1 == 1 and c2 == 1 and (a[n - 1] == b[0]):
        k = a[n - 1]
        for i in range(1, n - 1):
            m = a[i]
            n = b[i]
            if k <= m + n and m <= k + n and (n <= k + m):
                flag = False
            else:
                flag = True
                break
        if flag:
            print('No')
        else:
            print('Yes')
    else:
        print('No')
