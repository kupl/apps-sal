def solve(arr, n):
    a = [''] * n + arr[:] + [''] * n
    r = 0
    for i, e in enumerate(a):
        if e == 'D':
            for j in range(i - n, i + n + 1):
                if a[j] == 'C':
                    r += 1
                    a[j] = ''
                    break
    return r
