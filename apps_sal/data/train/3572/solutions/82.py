def invite_more_women(arr):
    women = 0
    for i in arr:
        if i == -1:
            women = women + 1
    if len(arr)%2 == 0:
        if women >= len(arr)//2:
            return False
        else:
            return True
    else:
        if women > len(arr)//2:
            return False
        else:
            return True


