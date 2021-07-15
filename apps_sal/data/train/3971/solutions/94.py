def tidyNumber(n):
    if n == int("".join(sorted(str(n)))):
        return True
    return False
