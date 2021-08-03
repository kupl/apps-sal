def tidyNumber(n):
    return [x for x in range(len(str(n)) - 1) if int(str(n)[x]) > int(str(n)[x + 1])] == []
