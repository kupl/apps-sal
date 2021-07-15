T = int(input())
while(T):
    xy = [int(x) for x in input().split()]
    st = 0
    n = xy[0] //xy[1]
    for i in range(1,n+1):
        st+=int(str(i*xy[1])[-1])
    print(st)
    T =T-1
