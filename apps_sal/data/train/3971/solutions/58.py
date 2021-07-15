def tidyNumber(n):
    n = list(map(str, str(n)))
    return sorted(n) == n
