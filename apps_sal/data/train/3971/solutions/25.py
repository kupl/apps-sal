def tidyNumber(n):
    for (idx, val) in enumerate(str(n)):
        if idx != 0:
            if val < str(n)[idx - 1]:
                return False
    return True
