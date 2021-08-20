def tidyNumber(n):
    n = str(n)
    print(n)
    for i in range(1, len(n)):
        if n[i] >= n[i - 1]:
            continue
        else:
            return False
    return True
