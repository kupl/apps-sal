t = int(input())
for tt in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    order = [1]
    ans = 0
    for i in range(1, n):
        num = i + 1
        index = 0
        if arr[i] > 0:
            index = order.index(arr[i])
            ans += min(index + 1, len(order) - index - 1)
            order.insert(index + 1, num)
        else:
            order.insert(0, num)
    print(ans)
