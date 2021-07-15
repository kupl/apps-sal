n = int(input())
p = list(map(int, input().split()))
s = list(map(int, input().split()))
a = [0]*n
a[0] = s[0]
g = [[] for _ in range(n+1)]
for i in range(n-1):
    g[p[i]].append(i+2)
for i in range(1, n):
    if s[i] == -1:
        if len(g[i+1]) == 0:
            s[i] = s[p[i-1]-1]
        else:
            m = s[g[i+1][0]-1]
            for j in g[i+1]:
                m = min(m, s[j-1])
            s[i] = m
    if s[i] < s[p[i-1]-1]:
        print(-1)
        return
    else:
        a[i] = s[i]-s[p[i-1]-1]
print(sum(a))

