n,m=map(int,input().split())
l=[]
leng=0
for i in range(n+m):
    w=int(input())
    if w==-1:
        cm=0
        mi=0
        for j in range(leng):
            if l[j]>cm:
                cm=l[j]
                mi=j
        
        print(cm)
        l[mi]=-1
    else:
        l.append(w)
        leng+=1
