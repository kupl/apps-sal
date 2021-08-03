for testcase in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    maxv, minv = max(arr), min(arr)
    print(maxv - minv + 2 * k)
