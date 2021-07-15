# cook your dish he

t=int(input())
while(t>0):
    a,b,c,d=map(int,input().rstrip().split())
    a1=abs(a-b)
    a2=abs(c-d)
    
    if a1==0 and a2==0:
        print("YES")
        
    elif a1==0 or a2==0:
        print("NO")
            
    elif a1>=a2:
        if a1%a2==0:
            print("YES")
        else:
            print("NO")    
    elif a2>a1:
        print("NO")    
    
    t-=1
