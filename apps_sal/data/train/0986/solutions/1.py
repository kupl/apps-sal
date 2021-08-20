t = int(input())
while t:
    t -= 1
    a = [int(i) for i in input().split()]
    n = int(a[0])
    k = int(a[1])
    flag = 1
    if k == 0:
        res = [i + 1 for i in range(n)]
    elif k > n / 2 or n % (2 * k) != 0:
        flag = 0
    else:
        temp1 = [i + 1 for i in range(k)]
        temp2 = [i + 1 for i in range(k, 2 * k)]
        temp = temp2 + temp1
        res = []
        x = n / (2 * k)
        while x:
            x -= 1
            res += temp
            temp = [i + 2 * k for i in temp]
    if flag:
        res = [str(i) for i in res]
        print(' '.join(res))
    else:
        print('CAPTAIN AMERICA EVADES')
