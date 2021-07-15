def tidyNumber(n):
    for i in range(len(str(n))-1):
        if not str(n)[i] <= str(n)[i+1]:
            return False
    return True
