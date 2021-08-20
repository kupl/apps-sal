for _ in range(int(input())):
    l = list(map(int, input().split()))
    h = (l[0] + l[1]) / 2
    k = (l[2] + l[3]) / 2
    if h >= k:
        print('{:.1f}'.format(h - k), 'DEGREE(S) ABOVE NORMAL')
    else:
        print('{:.1f}'.format(k - h), 'DEGREE(S) BELOW NORMAL')
