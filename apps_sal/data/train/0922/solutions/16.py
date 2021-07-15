# cook your dish here
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    d=list(map(int,input().split()))
    h=dict()
    for i in c:
        h[i]=h.get(i,0)+1
    for i in d:
        h[i]=h.get(i,0)+1
    k=list()
    for i,j in h.items():
        if j==1:k.append(i)
    k.sort()
    for i in k:
        print(i,end=" ")
    print()

