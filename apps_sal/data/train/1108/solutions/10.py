(n, m, k) = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
cnt = 0
for i in range(n):
    tot = sum(arr[i])
    q = arr[i][-1]
    tot -= q
    if tot >= m and q <= 10:
        cnt += 1
print(cnt)
