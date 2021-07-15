t=int(input())
for you in range(t):
    n=int(input())
    a=input().split()
    ai=[int(i) for i in a]
    b=input().split()
    bi=[int(i) for i in b]
    x=min(ai)
    y=min(bi)
    count=0
    for i in range(n):
        count+=max(ai[i]-x,bi[i]-y)
    print(count)

