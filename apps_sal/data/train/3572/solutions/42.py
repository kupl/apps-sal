def invite_more_women(arr):

  # No way this is the short way :(

    men = 0
    women = 0

    for x in arr:
        if x == 1:
            men += 1
        else:
            women += 1

    if women >= men:
        return False
    else:
        return True
