(n, x) = map(int, input().split())
a = list(map(int, input().split()))
b = []
i = 0
while i < n:
    j = i + 1
    while j <= n:
        b.append([sum(a[i:j]), i, j])
        j += 1
    i += 1
b.sort()
l = len(b)
v = b[l - 1][1]
y = b[l - 1][2]
z = b[l - 1][0]
print(float(sum(a[0:v]) + sum(a[y:n]) + z / x))
