def tidyNumber(n):
    n = str(n)
    for i in range(0, len(n) - 1):
        if n[i] > n[i + 1]:
            return False
    return True
