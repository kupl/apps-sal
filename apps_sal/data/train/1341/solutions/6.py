t = int(input())
for _ in range(t):
    n = int(input())
    data = list(map(int, input().strip().split()))
    prefix = [False] * n
    suffix = [False] * n
    prefix[0] = True
    for i in range(1, n):
        if data[i] > data[i - 1]:
            prefix[i] = True
        else:
            break
    suffix[n - 1] = True
    for i in range(n - 2, -1, -1):
        if data[i] < data[i + 1]:
            suffix[i] = True
        else:
            break
    ans = 0
    if prefix.count(True) == n:
        ans = n * (n - 1) / 2 + (n - 1)
    else:
        for i in range(n):
            if prefix[i]:
                low = i
                high = n
                while high - low > 1:
                    mid = (low + high) // 2
                    if suffix[mid] and data[i] < data[mid]:
                        high = mid
                    else:
                        low = mid
                ans += n - high
            else:
                break
        ans += suffix.count(True)
        ans += prefix.count(True)
    print(int(ans))
