for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    p = list(map(int, input().split()))
    window_sum = sum(p[:k])
    max_sum = window_sum
    for i in range(n - k):
        window_sum = window_sum - p[i] + p[i + k]
        max_sum = max(window_sum, max_sum)
    print(max_sum)
