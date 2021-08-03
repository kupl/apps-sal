def tidyNumber(n):
    a = str(n)
    for i in range(len(a) - 1):
        if int(a[i]) > int(a[i + 1]):
            return False
    return True
