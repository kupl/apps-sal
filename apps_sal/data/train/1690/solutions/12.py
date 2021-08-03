n, k = map(int, input().split())
l = [0]
vis = [0] * (n + 1)
for i in range(n):
    s = list(map(int, input().split(" ")))
    l.append(s[1:s[0] + 1])
q = []
q.append(1)
sol = 1
while(q != []):
    temp = q[0]
    q.pop(0)
    vis[temp] = 1
    for i in range(1, n + 1):
        if(vis[i] == 0):
            l1 = len(l[temp])
            l2 = len(l[i])
            len1 = l1 + l2
            slen1 = len(set(l[temp] + l[i]))
            if(len1 - slen1 >= k):
                vis[i] = 1
                sol += 1
                q.append(i)
print(sol)
