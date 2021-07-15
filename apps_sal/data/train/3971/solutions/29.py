def tidyNumber(n):
    for x in range(len(str(n)) - 1):
        if str(n)[x] <= str(n)[x + 1]:
            continue
        else:
            return False
    return True
