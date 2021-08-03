def choose(n, k):
    if k == 0:
        return 1
    else:
        return (n * choose(n - 1, k - 1)) // k
