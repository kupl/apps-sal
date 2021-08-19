t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    sum = 0
    for k in range(n // 2):
        sum = sum + abs(arr[n - k - 1] - arr[k])
    print(sum)
