n=int(input())
for i in range(n):
    l1=list(map(int,input().split()))
    b=min(l1[0],l1[1])
    g=max(l1[0],l1[1])
    sum1=g*2+(b-1)*2
    print(sum1)
    
    

