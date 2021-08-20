t = int(input())
for _ in range(t):
    n = int(input())
    (s, e) = (0, n)
    while s <= e:
        mid = (s + e) // 2
        if n >= 2 * mid * mid:
            ans = mid
            s = mid + 1
        else:
            e = mid - 1
    print(2 * ans)
