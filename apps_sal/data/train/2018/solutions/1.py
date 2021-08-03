# https://codeforces.com/problemset/problem/238/B
n, h = list(map(int, input().split()))
a = list(map(int, input().split()))
b = [[x, i] for i, x in enumerate(a)]
b = sorted(b, key=lambda x: x[0])


def solve(a, n, h):
    if n == 2:
        return 0, [1, 1]

    min_ = (a[-1][0] + a[-2][0]) - (a[0][0] + a[1][0])

    # move a[0] to 2th-group
    min_2 = max(a[-1][0] + a[-2][0], a[-1][0] + a[0][0] + h) - min(a[0][0] + a[1][0] + h, a[1][0] + a[2][0])

    ans = [1] * n
    if min_2 < min_:
        min_ = min_2
        ans[a[0][1]] = 2

    return min_, ans


min_, ans = solve(b, n, h)
print(min_)
print(' '.join([str(x) for x in ans]))

# 5 10
# 0 1 0 2 1

# 3 2
# 1 2 3
