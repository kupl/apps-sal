for i in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    s = sum(arr)
    print(max(int(s / k) + 1, n))
