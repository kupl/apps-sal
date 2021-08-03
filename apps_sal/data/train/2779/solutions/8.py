def fib_rabbits(n, b):
    if n < 2:
        return n
    ans = [0, 1]
    for i in range(2, n + 1):
        ans[0], ans[1] = ans[-1] * b, sum(ans)
    return ans[-1]
