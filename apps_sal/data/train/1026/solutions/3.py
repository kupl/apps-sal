mod = 1000000007
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[0] * (arr[1] - 1) * (arr[2] - 2) % mod)
