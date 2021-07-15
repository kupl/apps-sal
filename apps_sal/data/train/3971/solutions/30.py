def tidyNumber(n):
    n = list(str(n))
    n = [int(i) for i in n]
    sorted = n[:]
    sorted.sort()
    print(sorted)
    if n != sorted:
        return False
    else:
        return True
