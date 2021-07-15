n=int(input())
l=list(map(int,input().split()))
p=n
iss=set()
ans=[1]
out=1
for i in range(n) :
    if l[i]==p :
        p-=1
        while p in iss :
            p-=1
            out-=1
        ans.append(out)
    else :
        iss.add(l[i])
        out+=1
        ans.append(out)
print(*ans)
        
            
        
        
        
            
        

