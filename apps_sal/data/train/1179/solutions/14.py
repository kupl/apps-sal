t = int(input())
for _ in range(t):
    n = int(input())
    total_sum = (n * (n + 1)) // 2
    if total_sum % 2 != 0:
        print(0)
        continue

    l = 1
    r = n
    ans = 0

    while l + 1 < r:
        mid = (l + r) // 2
        prefix_sum = (mid * (mid + 1)) // 2
        suffix_sum = total_sum - prefix_sum
        if prefix_sum <= suffix_sum:
            l = mid
        else:
            r = mid

    ans += n - l
    if (l * (l + 1)) // 2 == total_sum // 2:
        ans += (l * (l - 1)) // 2 + ((n - l) * (n - l - 1)) // 2
    print(ans)
