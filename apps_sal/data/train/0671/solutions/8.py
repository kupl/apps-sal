for _ in range(int(input())):
    (n, s) = list(map(int, input().split()))
    p = list(map(int, input().split()))
    l = list(map(int, input().split()))
    one = 0
    zero = 0
    ans = 0
    mo = 10000000
    mz = 10000000
    for i in range(len(l)):
        if l[i] == 0:
            if p[i] < mz:
                mz = p[i]
        elif p[i] < mo:
            mo = p[i]
    ans = s + mo + mz
    if ans <= 100:
        print('yes')
    else:
        print('no')
