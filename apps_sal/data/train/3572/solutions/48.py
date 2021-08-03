def invite_more_women(arr):
    if len(arr) > 2 and len(arr) < 50:
        invitors = str(arr)
        a = invitors.count("1")
        n = invitors.count("-1")
        if a > n:
            return True
        else:
            return False
    else:
        return False
