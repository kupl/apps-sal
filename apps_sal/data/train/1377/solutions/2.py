for _ in range(int(input())):
    (a, b, c, d) = map(int, input().split())
    ans = a - c + (b - d)
    ans = ans / 2
    if ans < 0:
        temp = 'BELOW NORMAL'
    else:
        temp = 'ABOVE NORMAL'
    ans = abs(ans)
    print('{:.1f}'.format(ans), ' DEGREE(S) ', temp, sep='')
