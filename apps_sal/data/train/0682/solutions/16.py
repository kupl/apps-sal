n = int(input())
arr = list(map(int, input().split()))


def solve(arr, n):
    l = n
    for i in range(n):
        if arr[i] != i + 1:
            l = i + 1
            break
    if l == n:
        return [0, 0]
    r = 1
    for i in range(n - 1, 0, -1):
        if arr[i] != i + 1:
            r = i + 1
            break
    if r == 1:
        return [0, 0]
    if arr[l - 1:r] == [i for i in range(r, l - 1, -1)]:
        return [l, r]
    else:
        return [0, 0]


print(*solve(arr, n))
