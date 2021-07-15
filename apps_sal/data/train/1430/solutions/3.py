t=int(input())

r=[]
for each in range(t):
    n,k=list(map(int,input().split()))

    if n%2==0:
        r.append(n+n*k//2)
    else:
        n=n-1
        r.append(n+n*k//2+1+2*k)

for each in r:
    print(each)

