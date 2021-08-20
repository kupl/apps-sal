def fun(arr, n):
    cost = [0] * n
    cost[n - 1] = arr[n - 1]
    if n >= 2:
        cost[n - 2] = arr[n - 2]
        for i in range(n - 3, -1, -1):
            cost[i] = min(cost[i + 1], cost[i + 2]) + arr[i]
    return cost[0]


n = int(input())
a = list(map(int, input().split()))
b = list(reversed(a))
print(min(fun(a, n), fun(b, n)))
