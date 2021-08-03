# cook your dish here
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
    # 1 2 3 4 10
    # 1 3 6 10
    # 9 7 4 0

    # l for which ps<=ss
    # r for which ps>ss

    # prefix_sum>suffixsum--search in the left half
    # prefix_sum<suffixsum--search in the right half
    # prefix_sum==suffix_sum--stop
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
