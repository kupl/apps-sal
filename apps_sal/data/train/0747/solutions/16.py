def ans():
    n = int(input())
    a = list(map(int, input().split()))
    t = max(set(a), key=a.count)
    maxi = max(a)
    if a.count(maxi) > 1:
        print('NO')
        return
    cou = a.count(t)
    lis = []
    a.sort()
    b = set(a)
    if cou > 2:
        print('NO')
        return
    elif cou == 1:
        print('YES')
        for i in a:
            print(i, end=' ')
        print()
        return
    else:
        for i in b:
            if a.count(i) == 2:
                a.remove(i)
                lis.append(i)
            else:
                continue
    lis.sort(reverse=True)
    d = a + lis
    print('YES')
    for i in d:
        print(i, end=' ')
    print()
    return


t = int(input())
while t > 0:
    ans()
    t -= 1
