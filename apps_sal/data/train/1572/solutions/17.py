x = list(map(int, input().split()))
n = x[0]
a = x[1:n + 1]
p = x[n + 1:]
vis = [0] * n
parent = a[p.index(-1)]
vis[p.index(-1)] = 2
bhutiya = []
for i in range(n):
    if vis[i] != 2:
        vis[i] = 1
        rem = []
        rem.append(a[i])
        j = p[i] - 1
        while vis[j] != 2:
            rem.append(a[j])
            vis[j] = 1
            j = p[j] - 1
        rem.append(a[j])
        bhutiya.append(max(rem) - a[i])
print(max(bhutiya))
