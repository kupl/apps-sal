N,A,B = map(int,input().split())
X = list(map(int,input().split()))
dist = [0 for _ in range(N-1)]
for i in range(N-1):
    dist[i]=(X[i+1]-X[i])*A
cnt = 0
for i in range(N-1):
    if dist[i]>B:
        cnt +=B
    else:
        cnt += dist[i]
print(cnt)
