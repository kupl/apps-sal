def tidyNumber(n):
    n = str(n)
    for i in range(1,len(n)):
        if n[i-1] > n[i]:
            return False
    return True
