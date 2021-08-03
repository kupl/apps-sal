

def __starting_point():
    n = int(input())
    arr = list(map(int, input().split()))
    l = -1
    r = -1

    for i in range(n):
        if arr[i] != (i + 1):
            l = i

    for i in range(n - 1, 0, -1):
        if arr[i] != (i + 1):
            r = i

    sub = arr[r:l + 1]
    newarr = arr[:r] + sub[::-1] + arr[l + 1:]
    if arr == list(range(1, n + 1)):
        print("0 0")

    elif list(range(1, n + 1)) == newarr:
        print(r + 1, l + 1)

    else:
        print("0 0")


__starting_point()
