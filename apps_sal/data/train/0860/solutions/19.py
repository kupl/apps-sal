from math import ceil
T = int(input())
for a in range(T):
    N, H = map(int, input().split())
    A = list(map(int, input().split()))
    x = 1
    y = 10**9
    hr = 0
    k = 10000000000
    while x <= y:
        b = x + (y - x) // 2
        hr = 0
        for i in range(N):
            hr += ceil(A[i] / b)
        if hr <= H:
            k = min(k, b)
            y = b - 1
        else:
            x = b + 1
    print(k)
