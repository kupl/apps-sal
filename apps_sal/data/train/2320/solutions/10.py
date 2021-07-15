n = int(input())
a = list(map(int, input().split()))
b = list([(int(x[1]), x[0]) for x in enumerate(input().split())])
res = [0]*n
a.sort(reverse=True)
b.sort()
for i in range(n):
    res[b[i][1]] = a[i]
print(" ".join(map(str, res)))

