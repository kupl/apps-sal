for _ in range(int(input())):
    (n, m) = list(map(int, input().split()))
    s = input()
    r = c = 0
    arr = [0, 0, 0, 0]
    for i in s:
        if i == 'R':
            c += 1
        elif i == 'L':
            c -= 1
        elif i == 'U':
            r += 1
        elif i == 'D':
            r -= 1
        if r < 0:
            if arr[0] < abs(r):
                arr[0] = abs(r)
        elif arr[1] < r:
            arr[1] = r
        if c < 0:
            if arr[2] < abs(c):
                arr[2] = abs(c)
        elif arr[3] < c:
            arr[3] = c
    if arr[0] + arr[1] >= n or arr[2] + arr[3] >= m:
        print('unsafe')
    else:
        print('safe')
    r = c = 0
