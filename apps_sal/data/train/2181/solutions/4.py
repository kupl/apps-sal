n = int(input())


def get_cost(arr):
    cost = [0, 0]
    last = arr[0]
    for i in range(1, len(arr)):
        cost.append(cost[-1] + max(0, last + 1 - arr[i]))
        last = max(last + 1, arr[i])
    return cost


arr = list(map(int, input().split()))
left_cost, right_cost = get_cost(arr), get_cost(list(reversed(arr)))
ans = min(left_cost[n], right_cost[n])
for i in range(1, n - 1):
    ans = min(ans, max(left_cost[i] + right_cost[n - i], left_cost[i + 1] + right_cost[n - i - 1]))
print(ans)
