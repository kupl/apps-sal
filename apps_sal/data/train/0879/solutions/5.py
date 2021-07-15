t=int(input())
for i in range(t):
    x,y=list(map(int,input().split()))
    sum=0
    for j in range(int(x/y)+1):
            sum=sum+(j*y)%10
    print(sum)   

