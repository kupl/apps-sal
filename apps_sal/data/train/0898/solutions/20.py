for _ in range(0,int(input())):
    m,n=map(int,input().split())
    l=[9,99,999,9999,99999,999999,9999999,99999999]
    t=0
    if 9<=n<99:
        t=1
    elif 99<=n<999:
        t=2
    elif 999<=n<9999:
        t=3
    elif 9999<=n<99999:
        t=4
    elif 99999<=n<999999:
        t=5
    elif 999999<=n<9999999:
        t=6
    elif 9999999<=n<99999999:
        t=7
    elif 99999999<=n:
        t=8
    if t==0:
        print(0,0)
    else:
        print(m*t,m)
