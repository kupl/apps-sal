t=int(input())
for _ in range(t):
    n=int(input())
    c=0
    for i in range(n):
        ans=""
        c+=i+1
        for j in range(i+1):
            ans+=str(c)
            c-=1
        c+=i+1
        print(ans)
       
    
        
    
                
    

