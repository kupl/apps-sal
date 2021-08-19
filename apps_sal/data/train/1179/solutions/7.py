def binary_search(n, target):
    lo = 1
    hi = n
    while lo <= hi:
        mid = (lo + hi) // 2
        x = mid * (mid + 1) // 2
        if x < target:
            lo = mid + 1
        elif x > target:
            hi = mid - 1
        else:
            return (True, mid)
    return (False, hi)


def solve(n):
    m = n * (n + 1) // 2
    if m % 2 == 1:
        return 0
    (find, j) = binary_search(n, m // 2)
    ans = 0
    if find:
        k = n - j
        ans += j * (j - 1) // 2
        ans += k * (k - 1) // 2
    return ans + n - j


for _ in range(int(input())):
    n = int(input())
    print(solve(n))
