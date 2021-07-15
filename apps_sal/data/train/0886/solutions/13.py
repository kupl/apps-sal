t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(n):
        l[i]+=l[i]%3
    x=int(input())
    a=-1
    b=-1
    for i in l:
        if i>x:
            if b==-1:
                b=i
            else:
                b=min(b,i)
        if i<x:
            if a==-1:
                a=i
            else:
                a=max(a,i)
    print(a,b)
                
            
        
    
                
    

