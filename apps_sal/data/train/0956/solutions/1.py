def func(a, n):
    if n < 3:
        return 0
    res_arr = []
    for i in range(n):
        x = (a[i][0] + a[(i + 1) % n][0]) / 2
        y = (a[i][1] + a[(i + 1) % n][1]) / 2
        res_arr.append((x, y))
    l = len(res_arr)
    s = 0
    for i in range(n):
        u = res_arr[i][0] * res_arr[(i + 1) % l][1]
        v = res_arr[i][1] * res_arr[(i + 1) % l][0]
        s += (u - v)
    return abs(s) / 2


def __starting_point():
    n = int(input())
    arr = []
    for i in range(n):
        x, y = map(int, input().split())
        arr.append((x, y))

    res = func(arr, n)
    print(res)


__starting_point()
