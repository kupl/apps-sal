n, s = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]
arr.sort()
if (n == 1):
    print(abs(arr[0] - s))
else:
    if (arr[n // 2] == s):
        print(0)
    else:
        count = abs(s - arr[n // 2])
        arr[n // 2] = s
        for i in range(n // 2 + 1, n):
            if (arr[i] < arr[i - 1]):
                count += arr[i - 1] - arr[i]
                arr[i] = arr[i - 1]
        for i in range(n // 2 - 1, -1, -1):
            if (arr[i] > arr[i + 1]):
                count += arr[i] - arr[i + 1]
                arr[i] = arr[i + 1]
        print(count)
