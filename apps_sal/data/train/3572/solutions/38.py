def invite_more_women(arr):
    men = 0
    women = 0
    for x in arr:
        if x == 1:
            men += 1
        if x == -1:
            women += 1
    if women < men:
        return True
    return False
