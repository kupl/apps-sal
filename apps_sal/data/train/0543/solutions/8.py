# cook your dish here
t = int(input())
for i in range(t):
    truthtasks = []
    daretasks = []
    tr = int(input())
    TR = list(map(int, input().split()))
    dr = int(input())
    DR = list(map(int, input().split()))
    ts = int(input())
    TS = list(map(int, input().split()))
    ds = int(input())
    DS = list(map(int, input().split()))
    for i in TS:
        if i in TR:
            flag = 1
        else:
            flag = 0
            break
    if flag:
        for j in DS:
            if j in DR:
                flag = 1
            else:
                flag = 0
                break
    if flag:
        print('yes')
    else:
        print('no')
