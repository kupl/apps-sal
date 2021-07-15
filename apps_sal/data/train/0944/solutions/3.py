t=int(input())
while t!=0:
    t-=1
    n=int(input())
    li=list(map(int,input().split()))
    odd=[0]*n
    eve=[0]*n
    su=[0]*n
    ans=0
    x=0
    o=0
    e=0
    dic={}
    for i in range(n):
        x+=li[i]
        su[i]=x
        if li[i] not in dic:
            dic[li[i]]=[]
            dic[li[i]].append(i)
        else:
            dic[li[i]].append(i)
        if li[i]%2==0:
            e+=1
        else:
            o+=1
        eve[i]=e
        odd[i]=o
    for j in dic:
        if len(dic[j])==1:
            continue
        else:
            for o in range(0,len(dic[j])-1):
                fir=dic[j][o]
                sec=dic[j][o+1]
                if j%2==0:
                    if (eve[sec-1]-eve[fir])%2==0:
                        jk=su[sec-1]-su[fir]
                        
                        if jk>ans:
                            ans=jk
                else:
                    if (odd[sec-1]-odd[fir])%2!=0 and (odd[sec-1]!=0 or odd[fir]!=0):
                        jk=su[sec-1]-su[fir]
                        
                        if jk>ans:
                            ans=jk
    print(ans)
                    
                
                
                
            
        
    
    
        
            
                
    
    

