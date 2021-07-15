for _ in range(int(input())):
    t_r = int(input())
    tr = list(map(int, input().split()))
    d_r = int(input())
    dr = list(map(int, input().split()))
    t_s = int(input())
    ts = list(map(int, input().split()))
    d_s = int(input())
    ds = list(map(int, input().split()))
    
    flag = True
    
    for t in ts:
        if t not in tr:
            flag = False
            break
    
    if flag:
        for d in ds:
            if d not in dr:
                flag = False
                break
    
    print("yes" if flag else "no")
    
    
