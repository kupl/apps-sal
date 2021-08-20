x = list(map(int, input().split()))
n = x[0]
x = x[1:]
a = {i: x[i] for i in range(n)}
p = {i: x[n + i] for i in range(n)}
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
