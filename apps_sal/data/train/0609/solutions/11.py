for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    left = 0
    total_q = 0

    for i in range(n - 1):
        total_q += int(arr[i])
        total_q = total_q - k if total_q - k > 0 else 0
    left = total_q

    left += arr[n - 1]
    if left < k:
        print(n)
    elif left == k:
        print(n + 1)
    else:
        left = left - k
        print(n + int(left / k) + 1)
