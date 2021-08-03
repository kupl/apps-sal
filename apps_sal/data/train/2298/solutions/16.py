N, T = list(map(int, input().split()))
A = list(map(int, input().split()))

diff = -1
mini = A[0]
cnt = 0
ans = 0

for i in range(1, N):
    now = A[i]

    if mini > now:
        mini = now
    else:
        if now - mini == diff:
            cnt += 1
        elif now - mini > diff:
            diff = now - mini
            ans = max(ans, cnt)
            cnt = 1
ans = max(ans, cnt)
print(ans)
