for T in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    count = [0] * n

    for key in a:
        try:
            count[key - 1] += 1
        except:
            pass

    a = list(set(a))
    a.sort()

    flag = True
    for i in range(len(a)):
        if(a[i] != (i + 1)):
            flag = False
            mex = i + 1
            break
    if(flag):
        mex = len(a) + 1

    if(mex < m):
        print(-1)
    else:
        print(n - count[m - 1])
