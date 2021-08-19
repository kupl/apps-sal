def invite_more_women(arr):
    men = 0
    women = 0
    for x in arr:
        if x == 1:
            men += 1
        else:
            women += 1

    if men > women:
        return True
    else:
        return False
    # your code here
