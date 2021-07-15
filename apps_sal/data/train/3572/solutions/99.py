def invite_more_women(arr):
    women = arr.count(-1)
    man = arr.count(1)
    if man > women:
        return True
    else:
        return False
