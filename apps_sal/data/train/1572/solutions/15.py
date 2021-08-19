x = list(map(int, input().split()))

n = x[0]
a = x[1:n + 1]
p = x[n + 1:]
#vis = [0]*n

parent = a[p.index(-1)]
#vis[p.index(-1)] = 2

bhutiya = []

for i in range(n):
    if p[i] != -1:
        #vis[i] = 1
        #rem = []
        # rem.append(a[i])
        j = p[i] - 1
        maxi = a[i]

        while p[j] != -1:
            if a[j] > maxi:
                maxi = a[j]
            # rem.append(a[j])
            #vis[j] = 1
            j = p[j] - 1

        if a[j] > maxi:
            maxi = a[j]

        bhutiya.append(maxi - a[i])

print(max(bhutiya))
