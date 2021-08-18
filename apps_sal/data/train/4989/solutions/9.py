def hollow_triangle(n):
    ans = []
    for i in range(n - 1, 0, -1):
        x = '_' * i + '
        ans.append(x[:-1] + x[::-1])
    return ans + ['
