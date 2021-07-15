x=int(input())
t=[]
for i in range(x):
    q=list(map(int,input().split()))
    a=q[0]
    b=q[1]
    c=q[2]
    d=q[3]
    y=max(c,d)
    z=min(c,d)
    if(a==b):
        print("YES")
    elif(y==z):
        print("NO")
    elif((b-a)/(y-z)==(b-a)//(y-z)):
        print("YES")
    else:    
        print("NO")
            
    

