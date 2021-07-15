def tidyNumber(n):
    return all(int(a) <= int(b) for a, b in zip(str(n), str(n)[1:]))
