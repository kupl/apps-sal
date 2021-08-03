def solve(n, k):
    x = int(n / k)
    if x <= 1:
        return []

    def check(y):
        while y > 0:
            z = [i * y for i in range(1, k + 1)]
            if sum(z) == n:
                return z
            elif sum(z) < n:
                break
            elif sum(z) > n:
                pass
            y -= 1
        return z
    y = x
    z = check(y)
    mod = n - sum(z[:-1])
    if mod % z[0] == 0:
        return z[:-1] + [mod]
    while y > 0:
        y -= 1
        z = check(y)
        mod = n - sum(z[:-1])
        if mod % z[0] == 0:
            return z[:-1] + [mod]
