def tidyNumber(n):
    n = str(n)
    for i in range(len(n) - 1):
        if int(n[i]) > int(n[i + 1]):
            return False
            break
    return True
