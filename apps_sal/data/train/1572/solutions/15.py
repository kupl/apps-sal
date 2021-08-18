x = list(map(int, input().split()))

n = x[0]
a = x[1:n + 1]
p = x[n + 1:]

parent = a[p.index(-1)]

bhutiya = []

for i in range(n):
    if p[i] != -1:
        j = p[i] - 1
        maxi = a[i]

        while p[j] != -1:
            if a[j] > maxi:
                maxi = a[j]
            j = p[j] - 1

        if a[j] > maxi:
            maxi = a[j]

        bhutiya.append(maxi - a[i])

print(max(bhutiya))
