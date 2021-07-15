t=int(input())
for k in range(t):
    n=int(input())
    l=[int(i) for i in input().split()]
    m={}
    count=1
    for i in range(1,n):
        if l[i]==l[i-1]:
            count+=1
        else:
            
            if l[i-1] not in m:
                m[l[i-1]]=(count*(count+1))/2
            else:
                
                m[l[i-1]]+=(count*(count+1))/2
            count=1
    if(l[n-1]) not in m:
        m[l[n-1]]=(count*(count+1))/2
    else:
        
        m[l[n-1]]+=(count*(count+1))/2
    s=1
    
    for x in m:
        
         s=(s*m[x])%(1000000007)
    print(s)
    

