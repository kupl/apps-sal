for _ in range(int(input())):
    n=int(input())
    k={}
    for i in range(n):
        a,b=map(str,input().split())
        b=int(b)
        if a not in k:
            s=[0,0]
            if b==0:
                s[0]=1
            else:
                s[1]=1
            k[a]=s
        else:
            if b==0:
                k[a][0]+=1
            else:
                k[a][1]+=1
    c=0            
    for i in k.values():
        c+=max(i)
    print(c)    
        
                
