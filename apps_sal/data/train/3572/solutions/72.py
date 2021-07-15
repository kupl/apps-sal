def invite_more_women(arr):
    men = 0
    women = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            men += 1
        elif arr[i] == -1:
            women += 1
    if men > women:
        return True
    else:
        return False
