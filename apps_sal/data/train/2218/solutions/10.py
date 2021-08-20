n = int(input())
a = list(map(int, input().split()))
q = int(input())
arr = []
for _ in range(q):
    arr.append(list(map(int, input().split())))
arr.reverse()
ans = [-1] * n
cur = 0
for i in arr:
    if i[0] == 2:
        cur = max(cur, i[1])
    elif ans[i[1] - 1] == -1:
        ans[i[1] - 1] = max(cur, i[2])
for i in range(n):
    if ans[i] == -1:
        ans[i] = max(a[i], cur)
print(*ans)
