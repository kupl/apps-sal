n=int(input())
l=list(map(int,input().split()))
val=0
i=1
A,B=0,0
while i<=n:
    if i!=l[i-1]:
        p=l[i-1:l[i-1]]
        q=sorted(p,reverse=True)
        if p!=q:
            val+=1
            break 
        else:
            val+=1
            i=l[i-1]
            B=l[i-1]
            A=i
    i+=1
if val>1:
    print(0,0)
else:
    print(B,A)
