for _ in range(int(input())):
    t_r = int(input())
    tr = list(map(int, input().split()))
    d_r = int(input())
    dr = list(map(int, input().split()))
    t_s = int(input())
    ts = list(map(int, input().split()))
    d_s = int(input())
    ds = list(map(int, input().split()))
    l = []
    for i in ts:
        if i in tr:
            l.append('y')
        else:
            l.append('no')
    for i in ds:
        if i in dr:
            l.append('y')
        else:
            l.append('no')
    if "no" in l:
        print("no")
    else:
        print("yes")
