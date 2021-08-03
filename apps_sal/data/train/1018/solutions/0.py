
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    hrs = arr[0] - arr[1]

    for i in range(1, n - 1):
        if hrs > arr[i] - arr[i + 1]:
            hrs = arr[i] - arr[i + 1]

    print(hrs)
