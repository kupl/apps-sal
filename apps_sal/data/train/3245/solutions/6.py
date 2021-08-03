def checkchoose(m, n):
    for k in range(n + 1):
        nk = n - k
        ans = partial_fact(n, k) / factorial(nk) if k > nk else partial_fact(n, nk) / factorial(k)
        if m == ans:
            return k
        if m < ans:
            return -1  # No need to search the other side of the triangle
    return -1


f = [0, 1, 2, 6, 24, 120]


def factorial(n):
    if n == 0 or n == 1:
        return 1
    if n < len(f):
        return f[n]
    f.append(factorial(n - 1) * n)
    return f[n]


def partial_fact(hi, le): return 1 if hi <= le else hi * partial_fact(hi - 1, le)
