n = int(input())
perm = [0 for i in range(n)]
a = [[0 for i in range(n)] for i in range(n)]
b = [0 for i in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
    b[i] = max(a[i])

s = set()

for i in range(1, n + 1):
    for j in range(n):
        if b[j] <= i and j not in s:
            perm[j] = i
            s.add(j)
            break
print(*perm)
