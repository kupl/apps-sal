def pattern(n):
    return "\n".join(["".join([str(j % 10) for j in range(n, n - i, - 1)]).ljust(n, str((n - i) % 10)) for i in range(n)])
