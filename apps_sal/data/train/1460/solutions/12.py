try:
    n,x,y = map(int,input().split())
    shifts = list(map(int,input().split()))
    totel = x*n
    for i in shifts:
        tip = int(y *(1-(2*i)//100))
        totel += tip
    if totel <300:
        print('NO')
    else:
        print('YES')
except:
    pass
