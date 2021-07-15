def tidyNumber(n):
    o = str(n)[0]
    for i in str(n):
        if i >= o:
            o = i
        else:
            return False
    return True

