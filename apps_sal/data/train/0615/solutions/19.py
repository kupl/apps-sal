for _ in range(int(input())):
    (n, q) = map(int, input().split())
    arr = list(map(int, input().split()))
    prefix_sum = [0]
    for i in range(n):
        prefix_sum.append(prefix_sum[-1] + arr[i])
    for i in range(q):
        (x, y) = map(int, input().split())
        print(prefix_sum[y] - prefix_sum[x - 1])
