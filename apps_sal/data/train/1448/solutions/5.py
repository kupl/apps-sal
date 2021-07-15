# cook your dish here
t=int(input())
for i in range(t):
    a,d,k,n,inc=map(int,input().split())
    l=[a]
    for i in range(2,n+1):
        a+=d
        l.append(a)
        if i%k==0:
            d+=inc
    print(l[n-1])
