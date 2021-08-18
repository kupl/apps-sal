
n, k = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))


def solve(a, k):
    b = a[::-1]
    S = sum(a)
    n = len(a)
    div = S // n
    re = S % n
    T = 0

    num = re

    for i in range(n - 1, -1, -1):
        thres = div

        if num > 0:
            thres += 1
            num -= 1

        if a[i] > thres:
            T += a[i] - thres

    if k >= T:
        return 1 if re > 0 else 0

    l_arr = [0] * n
    r_arr = [0] * n

    for i in range(1, n):
        l_arr[i] = (a[i] - a[i - 1]) * i

    for i in range(1, n):
        r_arr[i] = (b[i - 1] - b[i]) * i

    remain = k
    l, u = a[0], b[0]

    for i in range(1, n):
        if remain >= l_arr[i]:
            remain -= l_arr[i]
            l = a[i]
        else:
            l += remain // i
            break

    remain = k

    for i in range(1, n):
        if remain >= r_arr[i]:
            remain -= r_arr[i]
            u = b[i]
        else:
            u -= remain // i
            break

    return u - l


print(solve(a, k))
