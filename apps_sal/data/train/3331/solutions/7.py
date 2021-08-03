def solve(arr, n):
    dc = n * ['x'] + arr[:] + n * ['x']
    p = 0
    ct = 0
    while p < len(dc):
        if dc[p] == 'D':
            for i in range(p - n, p + n + 1):
                if dc[i] == 'C':
                    dc[i] = 'X'
                    ct += 1
                    break
        p += 1
    return ct
