def rec(h, low, high):
    maxIndex = low
    for i in range(low + 1, high + 1):
        if h[i] > h[maxIndex]:
            maxIndex = i
    if maxIndex == low or maxIndex == high:
        return 1
    else:
        return 1 + min(rec(h, low, maxIndex - 1), rec(h, maxIndex + 1, high))


t = int(input())
for T in range(t):
    n = int(input())
    h = list(map(int, input().split()))
    print(rec(h, 0, n - 1))
