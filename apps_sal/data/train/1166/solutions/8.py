n=int(input())
x=list(map(int,input().split()))
q=int(input())
for i in range(q):
    c=0
    k=int(input())
    for j in range(n):
        for l in range(j,n):
            if(min(x[j:l+1])==k):
                c+=1
    print(c)

