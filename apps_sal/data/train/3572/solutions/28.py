def invite_more_women(arr):
    men = arr.count(1)
    women = arr.count(-1)
    if men <= women:
        return False
    return True
