T=int(input())

for _ in range(T):
    N=int(input())
    road=[]
    for _ in range(N):
        t=input()
        if t[0]=='B':
            road.append(('B',t[5:]))
        elif t[0]=='R':
            road.append(('R',t[5:]))
        else:
            road.append(('L',t[4:]))
    for x in range(N):
        Tprev, temp=road.pop()
        if x == 0:
            print('Begin' + temp)
        else:
            if prev == 'L':
                print('Right' + temp)
            else:
                print('Left' + temp)
        prev=Tprev
    print()

