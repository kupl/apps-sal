def series_sum(n):
    if n == 0:
        return "0.00"
    d = 1
    ans = 0
    for i in range(n):
        ans += 1/d
        d += 3
    ans = f"{round(ans, 2)}"
    return ans if len(ans) == 4 else ans + "0" * (4 - len(ans))
