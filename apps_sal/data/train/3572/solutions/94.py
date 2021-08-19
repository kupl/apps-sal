def invite_more_women(arr):
    men = []
    women = []
    for i in arr:
        if abs(i) == i:
            men.append(i)
        else:
            women.append(i)
    if len(men) > len(women):
        return True
    if len(men) <= len(women):
        return False
