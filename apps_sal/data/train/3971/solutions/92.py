def tidyNumber(n):
    result = True
    for i in range(len(str(n)) - 1):
        if int(str(n)[i + 1]) >= int(str(n)[i]):
            continue
        else:
            return False
    return result
