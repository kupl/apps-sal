(N, T) = map(int, input().split())
A = list(map(int, input().split()))
cnt = max_profit = 0
INF = float('inf')
min_cost = INF
for a in A:
    profit = a - min_cost
    if profit == max_profit:
        cnt += 1
    elif profit > max_profit:
        cnt = 1
        max_profit = profit
    min_cost = min(min_cost, a)
print(cnt)
