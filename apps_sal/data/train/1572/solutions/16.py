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
        j = p[i] - 1
        maxi = a[i]

        while vis[j] != 2:
            if a[j] > maxi:
                maxi = a[j]
            j = p[j] - 1

        if a[j] > maxi:
            maxi = a[j]

        bhutiya.append(maxi - a[i])

print(max(bhutiya))
