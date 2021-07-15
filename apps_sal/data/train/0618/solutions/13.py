for i in range(int(input())):
    n , k = map(int,input().split())
    li = list(map(int,input().split()))
    s = 0
    s = sum(li[0:k])
    m = s
    for i in range(n-1):
        if(k + i >= n):
            s = s - li[i] + li[k + i - n]
        else:
            s = s - li[i] + li[k + i]
        if(s > m):
            m = s
    print(m)
