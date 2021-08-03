def tidyNumber(n):
    n = str(n)

    if ''.join(sorted(n)) == n:
        return True
    else:
        return False
