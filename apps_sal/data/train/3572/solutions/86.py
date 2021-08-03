def invite_more_women(arr):
    women = []
    men = []
    for i in arr:
        if i == 1:
            men.append(i)
        else:
            women.append(i)
    if len(men) > len(women):
        return True
    else:
        return False
