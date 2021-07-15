# cook your dish here
n=int(input())
l=list(map(int,input().split()))
q=int(input())
for _ in range(q):
    x=int(input())
    c=0
    for i in range(n):
        for j in range(i+1,n+1):
            d=min(l[i:j])
            if(d==x):
                c+=1
    print(c)

