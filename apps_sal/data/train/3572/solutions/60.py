def invite_more_women(arr):
    women = 0
    men = 0
    for person in arr:
        if person == -1:
            women += 1
        if person == 1:
            men += 1
    return men > women
