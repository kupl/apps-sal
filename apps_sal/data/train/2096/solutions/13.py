n = int(input())
a = list(map(int,input().split()))
x = sorted([(a[i], i) for i in range(n)])
ans = []
visited = [False for i in range(n)]

for i in range(n):
    if visited[i]:
        continue
    cur = i
    cyc = []
    while not visited[cur]:
        visited[cur] = True
        cyc.append(cur + 1)
        cur = x[cur][1]
    ans.append(cyc)
 
print(len(ans))
for cyc in ans:
    print(len(cyc), ' '.join(map(str, cyc)))
