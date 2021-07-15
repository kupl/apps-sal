s,k = map(int,input().split())
a = str(s)
l = [int(d) for d in str(a)]
while k>0:
    for j in range(len(l)):
        if l[j]==9:
            continue
        else:
            l[j] = 9
            k-=1
        if k<1:
            break
print(*l,sep="")            
        
    
