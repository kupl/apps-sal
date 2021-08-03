def tidyNumber(n):
    for k, v in enumerate(str(n)):
        if k == 0:
            pass
        else:
            if v < str(n)[k - 1]:
                return False
    return True
