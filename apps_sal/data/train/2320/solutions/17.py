n = int(input())
a = sorted(list(map(int, input().split())), reverse = True)
b = list(map(int, input().split()))
c = sorted([(i, b[i]) for i in range(n)], key = lambda x : x[1])
res = [0] * n
for i in range(n):
    res[c[i][0]] = a[i]
print(*res)

