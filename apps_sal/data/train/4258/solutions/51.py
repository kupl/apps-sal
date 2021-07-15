def series_sum(n):
    ans = 0
    while n != 0:
        ans += 1 / (3 * n - 2)
        n -= 1
    return "{:.2f}".format(round(ans,2)).__str__()
