n, m, k = list(map(int, input().split()))
mat = []
for _ in range(n):
    arr = list(map(int, input().split()))
    mat.append(arr)


count = 0
for i in range(n):
    curr = 0
    for j in range(k):
        curr += mat[i][j]
    if mat[i][-1] <= 10 and curr >= m:
        count += 1

print(count)
