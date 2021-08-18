t = eval(input())

for i in range(t):
    n, m = list(map(int, input().split()))
    hsck = 0
    z = list(range(1, n + 1))

    z = z[m:] + z[:m]

    arr = {j: 0 for j in z}

    y = z[0]
    while arr[y] != 1:
        arr[y] = 1
        y = z[y - 1]
    c = 0
    for j in list(arr.keys()):
        c += arr[j]

    if c == n:
        print('Yes')
    else:
        print('No', c)
