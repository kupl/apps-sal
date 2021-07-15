def tidyNumber(n):
    n = str(n)
    k = list(map(int,n))
    l = sorted(k)
    if k == l:
        return True
    else:
        return False
