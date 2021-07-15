# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    q=int(input())
    for i in range(q):
        a,b=map(int,input().split())
        print(sum(l[a-1:b]))
