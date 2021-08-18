N, T = list(map(int, input().split()))
a = list(map(int, input().split()))
max_profit = 0
mini = a[0]
for i in range(1, N):
    max_profit = max(max_profit, a[i] - mini)
    mini = min(mini, a[i])
mini = a[0]
ans = 0
for i in range(1, N):
    if a[i] - mini == max_profit:
        ans += 1
    mini = min(mini, a[i])
print(ans)
