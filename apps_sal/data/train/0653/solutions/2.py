def game(n,l,p):
    if(len(l)==0):
        return 0
    l.sort()
    if(len(l)>=1 and p<l[0]):
        return 0
    l.sort()
    c=0
    
    
    ma=set()
    ma.add(0)
    while(len(l)):
        if(p>=l[0]):
            p-=l[0]
            
            c+=1
            ma.add(c)
            l=l[1:]
        else:
            if(c>0):
                c-=1
                ma.add(c)
                p+=l[-1]
                l=l[:-1]
            else:
                return max(ma)
    return max(ma)
            
            
            
        
        
n=int(input())
l=list(map(int,input().split()))
p=int(input())
print(game(n,l,p))

   

