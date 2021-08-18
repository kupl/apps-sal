t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    m = a[0]
    n1 = a[1]
    for i in range(0, n):
        if(m > n1):
            m = m - n1
            n1 = n1
        else:
            m = m
            n1 = n1 - m
    ans = m * n1
    if(ans > 0):
        print('Yes', ans)
    else:
        print('No')
    t -= 1
