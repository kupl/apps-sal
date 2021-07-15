N=int(input())
a=list(map(int,input().split()))

cnt=0
for i in range(N):
    cnt=cnt^a[i]

B=[]*N
for i in range(N):
    ans=cnt^a[i]
    B.append(str(ans))

print(' '.join(B))
