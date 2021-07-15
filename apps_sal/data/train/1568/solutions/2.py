t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    cnt=0
    for j in range(n):
        if l[j]>=n/2:
            cnt+=1
    print(cnt)
