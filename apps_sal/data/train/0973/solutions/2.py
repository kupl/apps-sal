for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    maxv = max(arr)
    minv = min(arr)
    print(abs((maxv + k) - (minv - k)))
