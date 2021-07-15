def invite_more_women(arr):
    men = 0
    women = 0
    for i in arr:
        if i == -1:
            women = women + 1
        elif i == 1:
            men = men + 1
        else:
            return False
    if women >= men:
        return False
    else:
        return True
