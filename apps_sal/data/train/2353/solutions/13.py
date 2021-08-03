n = int(input())
a = list(map(int, input().split()))


def solve(n, a):
    if n == 1:
        return [str(a[0])]

    arr = [[x, i] for i, x in enumerate(a)]
    arr = sorted(arr, key=lambda x: x[0])
    ans = [-1] * n

    for [x, i], [y, j] in zip(arr[1:], arr[:-1]):
        ans[j] = str(x)

    ans[arr[-1][1]] = str(arr[0][0])

    return ans


ans = solve(n, a)

print(' '.join(ans))
