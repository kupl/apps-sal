# cook your dish here
for u in range(int(input())):
    n,k=list(map(int,input().split()))
    l=list(map(int,input().split()))
    for i in range(n-1,-1,-1):
        r=k//l[i]
        k=r*l[i]
    print(k)

