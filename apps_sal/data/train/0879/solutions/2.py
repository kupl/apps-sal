for _ in range(int(input())):
    X,Y=list(map(int,input().split()))
    su=0
    for i in range(1,X+1):
        if (Y*i)>X:
            break
        su+=(Y*i)%10
    print(su)

