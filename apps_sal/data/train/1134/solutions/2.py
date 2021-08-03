t = int(input())
while(t > 0):
    nq = [int(x) for x in input().split()]
    q = [int(x) for x in input().split()]
    sol = 0
    flag = 0
    for i in range(0, nq[1]):
        sol += q[i]
    for i in range(nq[1], nq[0]):
        sol = sol - (q[i] // 2)
        if(sol < 0):
            flag += 1
            break
    if(flag == 1):
        print('DEFEAT')
    else:
        print('VICTORY')
    t = t - 1
