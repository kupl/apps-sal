for _ in range(int(input())):
    a=list(map(int,input().split()))
    num=0
    den=0
    k=1
    great=0
    for i in a:
        if i==-1:break
        else:
            if i>30:great+=1
            if i%2==0:
                num+=k*i
                den+=k
            k+=1
    print(great,'%.2f'%(num/den))
