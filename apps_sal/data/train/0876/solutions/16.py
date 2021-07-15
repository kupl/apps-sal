# cook your dish here\
t=int(input())
for i in range(t):
    n,k=list(map(int, input().split()))
    a= list(map(int, input().split()))
    m=max(a)
    n=min(a)
    d=m-n
    if(d<k):
        print("YES")
    else:
        print("NO")

