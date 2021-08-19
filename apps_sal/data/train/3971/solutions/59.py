def tidyNumber(n):
    s = 0
    if len(str(n)) > 1:
        for i in str(n):
            if int(i) >= s:
                s = int(i)
                continue
            else:
                return False
    return True
