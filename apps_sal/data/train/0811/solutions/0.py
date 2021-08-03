try:
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    forward = [0] * (n + 1)
    backward = [0] * (n + 1)
    backward[0] = arr[0]
    backward[1] = arr[0] + arr[1]
    for i in range(k, n):
        forward[i] = arr[i] + max(forward[i - 1], forward[i - 2])

    for i in range(2, n):
        backward[i] = arr[i] + max(backward[i - 1], backward[i - 2])

    ans = -float("Inf")
    for i in range(k - 1, n):
        ans = max(ans, forward[i] + backward[i] - arr[i])
    print(ans)
except Exception:
    pass
