# cook your dish here
t=int(input())
while t>0:
    n,q=list(map(int,input().split()))
    blst=[0]
    for i in range(1,65):
        blst.append(0)
    i=1
    while n>0:
        if n%2:
            blst[i]=1
        n//=2
        i+=1
    while q>0:
        n=int(input())
        if n==1:
            p=int(input())
            if blst[p]:
                print('ON')
            else:
                print('OFF')
        elif n==2:
            p=int(input())
            if blst[p]==0:
                blst[p]=1
        elif n==3:
            p=int(input())
            if blst[p]==1:
                blst[p]=0
        else:
            p,r=list(map(int,input().split()))
            if blst[p]!=blst[r]:
                blst[p]+=1
                blst[p]%=2
                blst[r]+=1
                blst[r]%=2
        q-=1
    t-=1

