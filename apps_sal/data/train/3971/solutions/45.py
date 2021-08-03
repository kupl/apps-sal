def tidyNumber(n):
    print(n)
    n = [int(x) for x in str(n)]
    prev = n[0]
    for i, x in enumerate(n[1:]):
        if x >= prev:
            prev = x
        else:
            return False
    return True
