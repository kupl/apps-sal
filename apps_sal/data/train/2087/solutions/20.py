(n, l, r, ql, qr) = map(int, input().split())
arr = [int(i) for i in input().split()]
mini = 10 ** 20
sm = sum(arr)
appaji = 0
curr = 0
for i in range(n + 1):
    if i > 0:
        curr += arr[i - 1]
    now = curr * l + (sm - curr) * r
    j = n - i
    if i > j:
        now += (i - j - 1) * ql
    if j > i:
        now += (j - i - 1) * qr
    mini = min(mini, now)
print(mini)
