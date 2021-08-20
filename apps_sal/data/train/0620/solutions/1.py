def solve(arr, n, k):
    if max(arr) <= k:
        return 0
    ans = 0
    m = -1
    f = 0
    i = 0
    j = -1
    while j < n - 1:
        if arr[j + 1] <= k:
            j += 1
        elif arr[j + 1] > k:
            if m == -1:
                m = arr[j + 1]
                f += 1
                j += 1
            elif arr[j + 1] == m:
                f += 1
                j += 1
            else:
                ans = max(ans, j - i + 1)
                while f:
                    if arr[i] == m:
                        f -= 1
                    i += 1
                m = -1
                f = 0
    ans = max(ans, j - i + 1)
    return ans


for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(solve(arr, n, k))
