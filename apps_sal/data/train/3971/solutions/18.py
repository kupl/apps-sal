def tidyNumber(n):
    before = list(str(n))
    after = sorted(before)
    if(after == before):
        return True
    else:
        return False
