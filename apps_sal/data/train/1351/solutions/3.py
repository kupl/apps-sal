t = int(input())

for _ in range(t):
    
    n = int(input())
    l = list(map(int,input().split()))
    
    for i in range(len(l)):
        
        if l[i]>=i:
        
            l[i] = i
            
        else:
            l[i]=0
            
    print(*l)
