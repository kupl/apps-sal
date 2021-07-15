def bill(p):
    sum=0
    t=0
    i=0
    m=0
    while 1:
        if sum==p:
            break
        elif sum<p:
            sum=sum+y[i]
            m=m+1
        elif sum>p:
            sum=sum-y[i]
            i=i+1
            m=m-1
    return m

y=[2048,1024,512,256,128,64,32,16,8,4,2,1]
n=int(input())
for i in range(n):
    p=int(input())
    print(bill(p))
