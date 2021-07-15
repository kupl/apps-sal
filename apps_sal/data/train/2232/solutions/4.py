n=int(input())
ret=2
q=2
for k in range(1,n+1):
    if(q%(k+1)!=0):
        q+=k+1-(q%(k+1))
    while 1:
        w=q*q
        if (w-ret)%k==0:
            print((w-ret)//k)
            ret=q
            break
        q+=k+1


